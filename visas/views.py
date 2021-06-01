from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .models import Visa
from .forms import VisaForm
from empleados.models import Empleado

class ListaVisa(PermissionRequiredMixin,ListView):
    permission_required = 'visas.view_visa'
    model = Visa
    success_message = "¡Visa editada con éxito!"
    context_object_name = 'visas'

class NuevaVisa(PermissionRequiredMixin,CreateView):
    permission_required = 'visas.add_visa'
    model = Visa
    form_class = VisaForm
    extra_context = {'editar': False}
    success_url = reverse_lazy('visas:lista')

    def post(self,request,*args,**kwargs):
        form = VisaForm(request.POST)
        if form.is_valid():
            visa = form.save()
            asesor = get_object_or_404(Empleado,username=request.user.username)
            visa.asesor_id = asesor.id
            visa.save()
        return redirect('visas:lista')

class DetalleVisa(PermissionRequiredMixin,DetailView):
    permission_required = 'visas.view_visa'
    model = Visa
    context_object_name = 'visa'

class EditarVisa(PermissionRequiredMixin,UpdateView,SuccessMessageMixin):
    permission_required = 'visas.change_visa'
    model = Visa
    form_class = VisaForm
    success_url = reverse_lazy('visas:lista')
    success_message = "Visa actualizada con éxito!"
    extra_context = {'editar': True}

class EliminarVisa(PermissionRequiredMixin,DeleteView):
    permission_required = 'visas.delete_visa'
    model = Visa
    success_url = reverse_lazy('visas:lista')
