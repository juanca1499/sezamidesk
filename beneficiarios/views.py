from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Beneficiario
from .forms import BeneficiarioForm
from django.urls import reverse_lazy


class BeneficiariosPrincipal(ListView):
    model = Beneficiario
    template_name = "beneficiarios_principal.html"

class BeneficiariosDetalle(DetailView):
    model = Beneficiario

class BeneficiariosEditar(UpdateView):
    model = Beneficiario
    form_class = BeneficiarioForm
    extra_context = {'etiqueta':'Actualizar datos del','boton':'Guardar'}
    success_url = reverse_lazy('beneficiarios:principal')