from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import AtencionMigrantes
from .forms import AtencionMigrantesForm
from beneficiarios.forms import BeneficiarioForm
from django.urls import reverse_lazy


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
    form_beneficiario = BeneficiarioForm
    extra_context = {'etiqueta':'Nuevo', 'boton':'Agregar', 'beneficiario_form':form_beneficiario}
    success_url = reverse_lazy('atencion_migrantes:principal')

