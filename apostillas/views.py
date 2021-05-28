from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Apostilla
from .forms import ApostillaForm

class ListaApostilla(ListView):
    model = Apostilla
    template_name = 'apostillas/apostilla_list.html'
    def get(self, request, *args, **kwargs):
        apostillas = Apostilla.objects.all()
        return render(request, self.template_name, {'apostillas': apostillas})

class NuevaApostilla(CreateView):
    model = Apostilla
    form_class = ApostillaForm
    success_url = reverse_lazy('apostillas:lista')

class DetalleApostilla(DetailView):
    model = Apostilla
    template_name = 'apostillas/apostilla_detail.html'

    def get(self, request, *args, **kwargs):
        apostilla = get_object_or_404(Apostilla,id=kwargs['pk'])
        return render(request, self.template_name, {'apostilla': apostilla})

class EditarApostilla(UpdateView):
    model = Apostilla
    success_url = reverse_lazy('apostillas:lista')

class EliminarApostilla(DeleteView):
    model = Apostilla
    success_url = reverse_lazy('apostillas:lista')