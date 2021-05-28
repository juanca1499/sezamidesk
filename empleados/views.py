from empleados.models import Empleado
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .forms import EmpleadoForm
from django.urls import reverse_lazy

from .models import Empleado

# Create your views here.

class EmpleadoList(ListView):
    model = Empleado   

class NuevoEmpleado(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    extra_context = {'etiqueta':'Nuevo','btn':'Agregar'}
    success_url = reverse_lazy('empleados:lista')

    def form_valid(self, form):
        user = form.save(commit=False)
        return super().form_valid(form)


