from empleados.models import Empleado
from django.shortcuts import render
from django.views.generic import ListView

from .models import Empleado

# Create your views here.

class EmpleadoList(ListView):
    model = Empleado   

    
