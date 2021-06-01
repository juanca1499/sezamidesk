from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .models import Apostilla
from .forms import ApostillaForm

class ListaApostilla(PermissionRequiredMixin,ListView):
    permission_required = 'apostillas.view_apostilla'
    model = Apostilla    
    success_message = "¡Apostilla editada con éxito!"
    context_object_name = 'apostillas'

class NuevaApostilla(PermissionRequiredMixin,CreateView):
    permission_required = 'apostillas.add_apostilla'
    model = Apostilla
    form_class = ApostillaForm
    extra_context = {'editar': False}
    success_url = reverse_lazy('apostillas:lista')

class DetalleApostilla(PermissionRequiredMixin,DetailView):
    permission_required = 'apostillas.view_apostilla'
    model = Apostilla
    context_object_name = 'apostilla'

class EditarApostilla(PermissionRequiredMixin,UpdateView,SuccessMessageMixin):
    permission_required = 'apostillas.change_apostilla'
    model = Apostilla
    form_class = ApostillaForm
    success_url = reverse_lazy('apostillas:lista')
    success_message = "Apostilla actualizada con éxito!"
    extra_context = {'editar': True}

class EliminarApostilla(PermissionRequiredMixin,DeleteView):
    permission_required = 'apostillas.delete_apostilla'
    model = Apostilla
    success_url = reverse_lazy('apostillas:lista')