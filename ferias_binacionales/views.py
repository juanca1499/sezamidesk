from django.shortcuts import render, redirect
from .models import * 
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import *

def servicios(request):
    return render(request,'menu_opciones.html')

# ----------------------------- Constancia de Estudios ---------------------------------
class ConstanciaEstudioList(ListView):
    model = ConstanciaEstudios
    template_name = 'ferias_binacionales/constancia_estudio/constancia_estudios_list.html'

class NuevaConstanciaEstudio(CreateView):
    model = ConstanciaEstudios
    form_class = ConstanciaEstudioForm
    extra_context = {'editar': False, 'boton':"Guardar"}
    template_name = 'ferias_binacionales/constancia_estudio/constanciaestudios_form.html'
    success_url = reverse_lazy('ferias_binacionales:constancia_estudios')

class DetalleConstanciaEstudio(DetailView):
    model = ConstanciaEstudios
    context_object_name = 'constancia'
    template_name = 'ferias_binacionales/constancia_estudio/constancia_estudios_detail.html'


# ----------------------------- Defensoria Pública ---------------------------------
class DefensoriaPublicaList(ListView):
    model = DefensoriaPublica
    template_name = 'ferias_binacionales/defensoria_publica/defensoria_publica_list.html'

class NuevaDefensoriaPublica(CreateView):
    model = DefensoriaPublica
    form_class = DefensoriaPublicaForm
    extra_context = {'editar': False, 'boton':"Guardar"}
    success_url = reverse_lazy('ferias_binacionales:defensoria_publica')
    template_name = 'ferias_binacionales/defensoria_publica/defensoria_publica_detail.html'

class DetalleDefensoriaPublica(DetailView):
    model = DefensoriaPublica
    context_object_name = 'defensoria'
    template_name = 'ferias_binacionales/defensoria_publica/defensoria_publica_detail.html'


# ----------------------------- Licencia de Conducir ---------------------------------
class LicenciaConducirList(ListView):
    model = LicenciaConducir
    template_name = 'ferias_binacionales/licencia_conducir/licencia_conducir_list.html'

class NuevaLicenciaConducir(CreateView):
    model = LicenciaConducir
    form_class = LicenciaConducirForm
    extra_context = {'editar': False, 'boton':"Guardar"}
    success_url = reverse_lazy('ferias_binacionales:licencia_conducir')
    template_name = 'ferias_binacionales/licencia_conducir/licenciaconducir_form.html'

class DetalleLicenciaConducir(DetailView):
    model = LicenciaConducir
    context_object_name = 'licencia'
    template_name = 'ferias_binacionales/licencia_conducir/licencia_conducir_detail.html'

# ----------------------------- Expedición de Acta de Nacimiento ---------------------------------
class ExpedicionActaList(ListView):
    model = ExpedicionActa
    template_name = 'ferias_binacionales/expedicion_acta/expedicion_acta_list.html'

class NuevaExpedicionActa(CreateView):
    model = ExpedicionActa
    form_class = ExpedicionActaForm
    extra_context = {'editar': False, 'boton':"Guardar"}
    success_url = reverse_lazy('ferias_binacionales:expedicion_acta')
    template_name = 'ferias_binacionales/expedicion_acta/expedicionacta_form.html'

class DetalleExpedicionActa(DetailView):
    model = ExpedicionActa
    context_object_name = 'acta'
    template_name = 'ferias_binacionales/expedicion_acta/expedicion_acta_detail.html'

# ----------------------------- Doble Nacional ---------------------------------
class DobleNacionalidadList(ListView):
    model = DobleNacionalidad
    template_name = 'ferias_binacionales/doble_nacionalidad/doble_nacionalidad_list.html'

class NuevaDobleNacionalidad(CreateView):
    model = DobleNacionalidad
    form_class = DobleNacionalidadForm
    extra_context = {'editar': False, 'boton':"Guardar"}
    template_name = 'ferias_binacionales/doble_nacionalidad/doblenacionalidad_form.html'
    success_url = reverse_lazy('ferias_binacionales:doble_nacionalidad')  

class DetalleDobleNacionalidad(DetailView):
    model = DobleNacionalidad
    context_object_name = 'nacionalidad'
    template_name = 'ferias_binacionales/doble_nacionalidad/doble_nacionalidad_detail.html'

# ----------------------------- Corrección de Acta de Nacimiento ---------------------------------
class CorreccionActaList(ListView):
    model = CorreccionActa
    template_name = 'ferias_binacionales/correccion_acta/correccion_acta_list.html'

class NuevaCorreccionActa(CreateView):
    model = CorreccionActa
    form_class = CorreccionActaForm
    extra_context = {'editar': False, 'boton':"Guardar"}
    template_name = 'ferias_binacionales/correccion_acta/correccionacta_form.html'
    success_url = reverse_lazy('ferias_binacionales:correccion_acta')

class DetalleCorreccionActa(DetailView):
    model = CorreccionActa
    context_object_name = 'correccion'
    template_name = 'ferias_binacionales/correccion_acta/correccion_acta_detail.html'
      
# ----------------------------- Mandamientos Judiciales ---------------------------------
class MandamientosJudicialesList(ListView):
    model = MandamientosJudiciales
    template_name = 'ferias_binacionales/mandamientos_judiciales/mandamientos_judiciales_list.html'

class NuevaMandamientosJudiciales(CreateView):
    model = MandamientosJudiciales
    form_class = MandamientosJudicialesForm
    extra_context = {'editar': False, 'boton':"Guardar"}
    success_url = reverse_lazy('ferias_binacionales:mandamiento_judicial')  
    template_name = 'ferias_binacionales/mandamientos_judiciales/mandamientosjudiciales_form.html'

class DetalleMandamientosJudiciales(DetailView):
    model = MandamientosJudiciales
    context_object_name = 'mand_jud'
    template_name = 'ferias_binacionales/mandamientos_judiciales/mandamientos_judiciales_detail.html'