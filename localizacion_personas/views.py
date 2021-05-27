from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy

class ListaPersonasDesaparecidas(PermissionRequiredMixin,ListView):
    model = PersonaDesaparecida
    paginate_by = 5
    extra_context = {'lp_lista':True}

class AgregarPersonaDesaparecida(PermissionRequiredMixin,CreateView):
    model = PersonaDesaparecida
    extra_context = {'etiqueta':'Nuevo','boton':'Agregar', 'lp_nuevo':True}
    success_url = reverse_lazy('localizacion_personas:lista')

class EditarPersonaDesaparecida(PermissionRequiredMixin,UpdateView):
    model = PersonaDesaparecida
    extra_context = {'etiqueta':'Actualizar','boton':'Guardar'}
    success_url = reverse_lazy('localizacion_personas:lista')

class Detalle(PermissionRequiredMixin,DetailView):
    model = PersonaDesaparecida