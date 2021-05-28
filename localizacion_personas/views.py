from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import PersonaDesaparecida
from .form import PersonaDesaparecidaForm

class ListaPersonasDesaparecidas(PermissionRequiredMixin,ListView):
    model = PersonaDesaparecida
    extra_context = {'lp_lista':True}

class AgregarPersonaDesaparecida(PermissionRequiredMixin,CreateView):
    model = PersonaDesaparecida
    form_class = PersonaDesaparecidaForm
    extra_context = {'etiqueta':'Nuevo','boton':'Agregar', 'lp_nuevo':True}
    success_url = reverse_lazy('localizacion_personas:lista')

class EditarPersonaDesaparecida(PermissionRequiredMixin,UpdateView):
    model = PersonaDesaparecida
    form_class = PersonaDesaparecidaForm
    extra_context = {'etiqueta':'Actualizar','boton':'Guardar'}
    success_url = reverse_lazy('localizacion_personas:lista')

class DetallePersonaDesaparecida(PermissionRequiredMixin,DetailView):
    model = PersonaDesaparecida