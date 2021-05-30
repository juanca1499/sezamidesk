from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import PersonaDesaparecida
from .forms import PersonaDesaparecidaForm

class ListaPersonasDesaparecidas(ListView):
    model = PersonaDesaparecida
    context_object_name = 'personas'
    extra_context = {'lp_lista':True}

class AgregarPersonaDesaparecida(CreateView):
    model = PersonaDesaparecida
    form_class = PersonaDesaparecidaForm
    extra_context = {'etiqueta':'Registrar','boton':'Registrar', 'lp_nuevo':True}
    success_url = reverse_lazy('localizacion_personas:lista')

class EditarPersonaDesaparecida(UpdateView):
    model = PersonaDesaparecida
    form_class = PersonaDesaparecidaForm
    extra_context = {'etiqueta':'Editar','boton':'Guardar'}
    success_url = reverse_lazy('localizacion_personas:lista')

class DetallePersonaDesaparecida(DetailView):
    model = PersonaDesaparecida
    context_object_name = "persona"

class EliminarPersonaDesaparecida(DeleteView):
    model = PersonaDesaparecida
    success_url = reverse_lazy('localizacion_personas:lista')