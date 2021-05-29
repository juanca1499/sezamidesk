from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Apostilla
from .forms import ApostillaForm

class ListaApostilla(ListView):
    model = Apostilla    
    context_object_name = 'apostillas'

class NuevaApostilla(CreateView):
    model = Apostilla
    form_class = ApostillaForm
    extra_context = {'editar': False}
    success_url = reverse_lazy('apostillas:lista')

class DetalleApostilla(DetailView):
    model = Apostilla
    context_object_name = 'apostilla'

class EditarApostilla(UpdateView):
    model = Apostilla
    form_class = ApostillaForm
    success_url = reverse_lazy('apostillas:lista')
    extra_context = {'editar': True}

    # def get(self, request, *args, **kwargs):
    #     apostilla = get_object_or_404(Apostilla,id=kwargs['pk'])
    #     return render(request,self.template_name,{'apostilla': apostilla,
    #                                               'editar': True})

    # def post(self, request, *args, **kwargs):
    #     apostilla = get_object_or_404(Apostilla,id=kwargs['pk'])
    #     if 'acta_americana' in request.POST:
    #         apostilla.acta_americana = True
    #     else:
    #         apostilla.acta_americana = False
    #     if 'acta_mexicana' in request.POST:
    #         apostilla.acta_mexicana = True
    #     else:
    #         apostilla.acta_mexicana = False
    #     if 'identificacion_padres' in request.POST:
    #         apostilla.identificacion_padres = True
    #     else:
    #         apostilla.identificacion_padres = False 
    #     if 'curp' in request.POST:
    #         apostilla.curp = True
    #     else:
    #         apostilla.curp = False
    #     if 'comprobante_domicilio' in request.POST:
    #         apostilla.comprobante_domicilio = True
    #     else:
    #         apostilla.comprobante_domicilio = False
    #     if 'rfc' in request.POST:
    #         apostilla.rfc = True
    #     else:
    #         apostilla.rfc = False
        
    #     apostilla.save()
    #     return redirect('apostillas:lista')

class EliminarApostilla(DeleteView):
    model = Apostilla
    success_url = reverse_lazy('apostillas:lista')