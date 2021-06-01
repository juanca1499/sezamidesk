from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import AtencionMigrantes
from .forms import AtencionMigrantesForm
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
    extra_context = {'etiqueta':'Nuevo', 'boton':'Agregar'}
    success_url = reverse_lazy('atencion_migrantes:principal')

