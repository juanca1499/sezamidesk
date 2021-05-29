from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .models import Visa

class ListaVisa(ListView):
    model = Visa
    # success_message = "¡Visa editada con éxito!"
    context_object_name = 'visas'

class NuevaVisa(CreateView):
    model = Visa
    # form_class = ApostillaForm
    extra_context = {'editar': False}
    success_url = reverse_lazy('visas:lista')

class DetalleVisa(DetailView):
    model = Visa
    context_object_name = 'visa'

class EditarVisa(UpdateView,SuccessMessageMixin):
    model = Visa
    # form_class = ApostillaForm
    success_url = reverse_lazy('visas:lista')
    # success_message = "Apostilla actualizada con éxito!"
    extra_context = {'editar': True}

class EliminarVisa(DeleteView):
    model = Visa
    success_url = reverse_lazy('visas:lista')
