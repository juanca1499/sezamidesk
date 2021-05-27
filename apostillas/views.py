from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Apostilla

class ListaApostilla(PermissionRequiredMixin,ListView):
    model = Apostilla

    def get(self, request, *args, **kwargs):
        lista_grupos = Apostilla.objects.all()

class NuevaApostilla(PermissionRequiredMixin,CreateView):
    model = Apostilla
    success_url = reverse_lazy('apostillas:lista')

class DetalleApostilla(PermissionRequiredMixin,DetailView):
    model = Apostilla

class EditarApostilla(PermissionRequiredMixin,UpdateView):
    model = Apostilla
    success_url = reverse_lazy('apostillas:lista')

class EliminarApostilla(PermissionRequiredMixin,DeleteView):
    model = Apostilla
    success_url = reverse_lazy('apostillas:lista')