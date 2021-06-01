from django.shortcuts import render, redirect
from .models import * 
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin

def servicios(request):
    return render(request,'menu_opciones.html')

class ConstanciaEstudioList(ListView):
    model = ConstanciaEstudios
    template_name = 'ferias_binacionales/constancia_estudios_list.html'

class DefensoriaPublicaList(ListView):
    model = DefensoriaPublica
    template_name = 'ferias_binacionales/defensoria_publica_list.html'

class LicenciaConducirList(ListView):
    model = LicenciaConducir
    template_name = 'ferias_binacionales/licencia_conducir_list.html'

class ExpedicionActaList(ListView):
    model = ExpedicionActa
    template_name = 'ferias_binacionales/expedicion_acta_list.html'

class DobleNacionalidadList(ListView):
    model = DobleNacionalidad
    template_name = 'ferias_binacionales/doble_nacionalidad_list.html'
    
class CorreccionActaList(ListView):
    model = CorreccionActa
    template_name = 'ferias_binacionales/correccion_acta_list.html'

class MandamientosJudicialesList(ListView):
    model = MandamientosJudiciales
    template_name = 'ferias_binacionales/mandamientos_judiciales_list.html'