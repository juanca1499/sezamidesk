from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Apostilla

class ListaApostilla(ListView):
    model = Apostilla
    lista_grupos = Apostilla.objects.all()

class NuevaApostilla(CreateView):
    model = Apostilla
    success_url = reverse_lazy('apostillas:lista')

class DetalleApostilla(DetailView):
    model = Apostilla

class EditarApostilla(UpdateView):
    model = Apostilla
    success_url = reverse_lazy('apostillas:lista')

class EliminarApostilla(DeleteView):
    model = Apostilla
    success_url = reverse_lazy('apostillas:lista')