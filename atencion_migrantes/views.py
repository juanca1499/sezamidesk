from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import AtencionMigrantes
from beneficiarios.models import Beneficiario, BeneficiarioDireccion, EstudioSocioeconomico
from beneficiarios.forms import BeneficiarioForm, BeneficiarioDireccionForm, EstudioSocioeconomicoForm
from tramites.models import Tramite
from empleados.models import Empleado
from .forms import AtencionMigrantesForm
from tramites.forms import PedirCurpForm


class AtencionMigrantesPrincipal(ListView):
    model = AtencionMigrantes
    template_name = "atencion_migrantes_principal.html"

class AtencionMigrantesDetalle(DetailView):
    model = AtencionMigrantes

class AtencionMigrantesEliminar(DeleteView):
    model = AtencionMigrantes
    success_url = reverse_lazy('atencion_migrantes:principal')

class AtencionMigrantesNuevo(CreateView):
    model = AtencionMigrantes
    form_class = AtencionMigrantesForm
    form_direccion = BeneficiarioDireccionForm
    form_estudio = EstudioSocioeconomicoForm
    template_name = "atencion_migrantes/atencionmigrantes_form.html"
    form_beneficiario = BeneficiarioForm
    extra_context = {
        'etiqueta':'Nuevo', 
        'boton':'Agregar', 
        'form_direccion':form_direccion,
        'form_estudio':form_estudio,
        'form_beneficiario':form_beneficiario,
    }
    success_url = reverse_lazy('atencion_migrantes:principal')

    def post(self,request,*args,**kwargs):
        curp = request.POST['curp']
        # Se verifica si hay un trámite pendiente con esa curp.
        # estado_tramite = tramite.estado_id

        cant_tramites = AtencionMigrantes.objects.filter(curp=curp, tramite__estado_id=1).count() # ...
        
        if cant_tramites == 0:
            # Se crea el trámite general
            tramite = Tramite()
            tramite.estado_id = 1
            # Se asigna el empleado que atiende el trámite
            empleado = get_object_or_404(Empleado,username=request.user.username)
            tramite.empleado_id = empleado.id
            tramite.save()
            tramite = Tramite.objects.latest('fecha_inicio')

            
            # Se crea el trámite específico
            atencion_migrantes = AtencionMigrantes()
            atencion_migrantes.curp = curp
            atencion_migrantes.tramite_id = tramite.id
            atencion_migrantes.save()
            return render(request,self.template_name,self.extra_context)
        else:
            beneficiario = Beneficiario()
            beneficiario.curp = curp
            estudio = EstudioSocioeconomico()
            direccion = BeneficiarioDireccion()
            form_beneficiario = BeneficiarioForm(instance=beneficiario)
            form_direccion = BeneficiarioDireccionForm(instance=direccion)
            form_estudio = EstudioSocioeconomicoForm(instance=estudio)
            return render(request,self.template_name,self.extra_context)


def pedir_curp(request):
    if request.method == "GET":
        form = PedirCurpForm()
        extra_context = {'form':form,
                         'app':'atencion_migrantes:nuevo'}
        return render(request,'tramites/pedir_curp.html',extra_context)