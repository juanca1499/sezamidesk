from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, View
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Tramite
from beneficiarios.models import Beneficiario
from .forms import PedirCurpForm
from beneficiarios.forms import BeneficiarioForm

class TramiteList(ListView):
    model = Tramite
    template_name= 'tramites/tramite_list.html'

    #def get(self, request, *args, **kwargs):
    #    lista_grupos = Tramite.objects.all()

def pedir_curp(request):
    if request.method == "GET":
        form = PedirCurpForm()
        extra_context = {'form':form}
        return render(request,'tramites/pedir_curp.html',extra_context)
    elif request.method == "POST":
        curp = request.POST['curp']
        cant_beneficiarios = Beneficiario.objects.filter(curp=curp).count()
        beneficiario = Beneficiario()
        if cant_beneficiarios == 0:
            beneficiario.curp = curp
            form = BeneficiarioForm(instance=beneficiario)
            return render(request,'beneficiarios/beneficiario_form.html',{'beneficiario':beneficiario,
                                                                          'form':form,
                                                                          'curp':curp,
                                                                          'etiqueta':'Registrar nuevo',
                                                                          'boton':'Guardar'})
        else:
            beneficiario = Beneficiario.objects.get(curp=curp)
            form = BeneficiarioForm(instance=beneficiario) 
            return render(request,'beneficiarios/beneficiario_form.html',{'beneficiario':beneficiario,
                                                                          'form':form,
                                                                          'curp':curp,
                                                                          'etiqueta':'Registrar nuevo',
                                                                          'boton':'Guardar'})
