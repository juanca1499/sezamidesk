from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Beneficiario
from .forms import BeneficiarioForm, BeneficiarioDireccionForm, EstudioSocioeconomicoForm
from django.urls import reverse_lazy


class BeneficiariosPrincipal(ListView):
    model = Beneficiario
    template_name = "beneficiarios_principal.html"

class BeneficiariosDetalle(DetailView):
    model = Beneficiario
    

class BeneficiariosEditar(UpdateView):
    model = Beneficiario
    form_beneficiario = BeneficiarioForm
    form_vivienda = BeneficiarioViviendaForm
    form_estudio = EstudioSocioeconomicoForm

    extra_context = {
        'etiqueta':'Actualizar datos del',
        'boton':'Guardar',
        'beneficario_form':form_beneficiario,
        'vivienda_form':form_vivienda,
        'estudio_form':form_estudio,
    }
    success_url = reverse_lazy('beneficiarios:principal')

class BeneficiariosCrear(CreateView):
    model = Beneficiario
    form_beneficiario = BeneficiarioForm
    form_vivienda = BeneficiarioViviendaForm
    form_estudio = EstudioSocioeconomicoForm
    extra_context = {
        'etiqueta':'Registrar nuevo',
        'boton':'Guardar',
         'beneficario_form':form_beneficiario,
        'vivienda_form':form_vivienda,
        'estudio_form':form_estudio,
    }
    success_url = reverse_lazy('beneficiarios:principal')

class BeneficiariosEliminar(DeleteView):
    model = Beneficiario
    success_url = reverse_lazy('beneficiarios:principal')
