from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import PersonaDesaparecida
from .forms import PersonaDesaparecidaForm

class ListaPersonasDesaparecidas(PermissionRequiredMixin,ListView):
    permission_required = 'localizacion_personas.view_personadesaparecida'
    model = PersonaDesaparecida
    context_object_name = 'personas'

class AgregarPersonaDesaparecida(PermissionRequiredMixin,CreateView):
    permission_required = 'localizacion_personas.add_personadesaparecida'
    model = PersonaDesaparecida
    form_class = PersonaDesaparecidaForm
    extra_context = {'etiqueta':'Registrar','boton':'Registrar'}
    success_url = reverse_lazy('localizacion_personas:lista')

class EditarPersonaDesaparecida(PermissionRequiredMixin,UpdateView):
    permission_required = 'localizacion_personas.change_personadesaparecida'
    model = PersonaDesaparecida
    form_class = PersonaDesaparecidaForm
    extra_context = {'etiqueta':'Editar','boton':'Guardar'}
    success_url = reverse_lazy('localizacion_personas:lista')

class DetallePersonaDesaparecida(PermissionRequiredMixin,DetailView):
    permission_required = 'localizacion_personas.view_personadesaparecida'
    model = PersonaDesaparecida
    context_object_name = "persona"

class EliminarPersonaDesaparecida(PermissionRequiredMixin,DeleteView):
    permission_required = 'localizacion_personas.delete_personadesaparecida'
    model = PersonaDesaparecida
    success_url = reverse_lazy('localizacion_personas:lista')