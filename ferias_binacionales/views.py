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
class ConstanciaEstudioList(PermissionRequiredMixin,ListView):
    permission_required = 'ferias_binacionales.view_constanciaestudio'
    model = ConstanciaEstudios
    template_name = 'ferias_binacionales/constancia_estudio/constancia_estudios_list.html'

class NuevaConstanciaEstudio(PermissionRequiredMixin,CreateView):
    permission_required = 'ferias_binacionales.add_constanciaestudio'
    model = ConstanciaEstudios
    form_class = ConstanciaEstudioForm
    extra_context = {'editar': False, 'boton':"Guardar"}
    template_name = 'ferias_binacionales/constancia_estudio/constanciaestudios_form.html'
    success_url = reverse_lazy('ferias_binacionales:constancia_estudios')

class DetalleConstanciaEstudio(PermissionRequiredMixin,DetailView):
    permission_required = 'ferias_binacionales.view_constanciaestudio'
    model = ConstanciaEstudios
    context_object_name = 'constancia'
    template_name = 'ferias_binacionales/constancia_estudio/constancia_estudios_detail.html'

class ActualizarConstanciaEstudio(PermissionRequiredMixin,UpdateView):
    permission_required = 'ferias_binacionales.change_constanciaestudio'
    model = ConstanciaEstudios
    form_class = ConstanciaEstudioForm
    extra_context = {'editar': True, 'boton':"Actualizar"}
    template_name = 'ferias_binacionales/constancia_estudio/constanciaestudios_form.html'
    success_url = reverse_lazy('ferias_binacionales:constancia_estudios')

class EliminarConstanciaEstudio(PermissionRequiredMixin,DeleteView):
    permission_required = 'ferias_binacionales.delete_constanciaestudio'
    model = ConstanciaEstudios
    success_url = reverse_lazy('ferias_binacionales:constancia_estudios')

# ----------------------------- Defensoria Pública ---------------------------------
class DefensoriaPublicaList(PermissionRequiredMixin,ListView):
    permission_required = 'ferias_binacionales.view_defensoriapublica'
    model = DefensoriaPublica
    template_name = 'ferias_binacionales/defensoria_publica/defensoria_publica_list.html'

class NuevaDefensoriaPublica(PermissionRequiredMixin,CreateView):
    permission_required = 'ferias_binacionales.add_defensoriapublica'
    model = DefensoriaPublica
    form_class = DefensoriaPublicaForm
    extra_context = {'editar': False, 'boton':"Guardar"}
    success_url = reverse_lazy('ferias_binacionales:defensoria_publica')
    template_name = 'ferias_binacionales/defensoria_publica/defensoriapublica_form.html'

class DetalleDefensoriaPublica(PermissionRequiredMixin,DetailView):
    permission_required = 'ferias_binacionales.view_defensoriapublica'
    model = DefensoriaPublica
    context_object_name = 'defensoria'
    template_name = 'ferias_binacionales/defensoria_publica/defensoria_publica_detail.html'

class ActualizarDefensoriaPublica(PermissionRequiredMixin,UpdateView):
    permission_required = 'ferias_binacionales.change_defensoriapublica'
    model = DefensoriaPublica
    form_class = DefensoriaPublicaForm
    extra_context = {'editar': True, 'boton':"Actualizar"}
    template_name = 'ferias_binacionales/defensoria_publica/defensoriapublica_form.html'
    success_url = reverse_lazy('ferias_binacionales:defensoria_publica')

class EliminarDefensoriaPublica(PermissionRequiredMixin,DeleteView):
    permission_required = 'ferias_binacionales.delete_defensoriapublica'
    model = DefensoriaPublica
    success_url = reverse_lazy('ferias_binacionales:defensoria_publica')


# ----------------------------- Licencia de Conducir ---------------------------------
class LicenciaConducirList(PermissionRequiredMixin,ListView):
    permission_required = 'ferias_binacionales.view_licenciaconducir'
    model = LicenciaConducir
    template_name = 'ferias_binacionales/licencia_conducir/licencia_conducir_list.html'

class NuevaLicenciaConducir(PermissionRequiredMixin,CreateView):
    permission_required = 'ferias_binacionales.add_licenciaconducir'
    model = LicenciaConducir
    form_class = LicenciaConducirForm
    extra_context = {'editar': False, 'boton':"Guardar"}
    success_url = reverse_lazy('ferias_binacionales:licencia_conducir')
    template_name = 'ferias_binacionales/licencia_conducir/licenciaconducir_form.html'

class DetalleLicenciaConducir(PermissionRequiredMixin,DetailView):
    permission_required = 'ferias_binacionales.view_licenciaconducir'
    model = LicenciaConducir
    context_object_name = 'licencia'
    template_name = 'ferias_binacionales/licencia_conducir/licencia_conducir_detail.html'

class ActualizarLicenciaConducir(PermissionRequiredMixin,UpdateView):
    permission_required = 'ferias_binacionales.change_licenciaconducir'
    model = LicenciaConducir
    form_class = LicenciaConducirForm
    extra_context = {'editar': True, 'boton':"Actualizar"}
    template_name = 'ferias_binacionales/licencia_conducir/licenciaconducir_form.html'
    success_url = reverse_lazy('ferias_binacionales:licencia_conducir')

class EliminarLicenciaConducir(PermissionRequiredMixin,DeleteView):
    permission_required = 'ferias_binacionales.delete_licenciaconducir'
    model = LicenciaConducir
    success_url = reverse_lazy('ferias_binacionales:licencia_conducir')


# ----------------------------- Expedición de Acta de Nacimiento ---------------------------------
class ExpedicionActaList(PermissionRequiredMixin,ListView):
    permission_required = 'ferias_binacionales.view_expedicionacta'
    model = ExpedicionActa
    template_name = 'ferias_binacionales/expedicion_acta/expedicion_acta_list.html'

class NuevaExpedicionActa(PermissionRequiredMixin,CreateView):
    permission_required = 'ferias_binacionales.add_expedicionacta'
    model = ExpedicionActa
    form_class = ExpedicionActaForm
    extra_context = {'editar': False, 'boton':"Guardar"}
    success_url = reverse_lazy('ferias_binacionales:expedicion_acta')
    template_name = 'ferias_binacionales/expedicion_acta/expedicionacta_form.html'

class DetalleExpedicionActa(PermissionRequiredMixin,DetailView):
    permission_required = 'ferias_binacionales.view_expedicionacta'
    model = ExpedicionActa
    context_object_name = 'acta'
    template_name = 'ferias_binacionales/expedicion_acta/expedicion_acta_detail.html'

class ActualizarExpedicionActa(PermissionRequiredMixin,UpdateView):
    permission_required = 'ferias_binacionales.change_expedicionacta'
    model = ExpedicionActa
    form_class = ExpedicionActaForm
    extra_context = {'editar': True, 'boton':"Actualizar"}
    success_url = reverse_lazy('ferias_binacionales:expedicion_acta')
    template_name = 'ferias_binacionales/expedicion_acta/expedicionacta_form.html'

class EliminarExpedicionActa(PermissionRequiredMixin, DeleteView):
    permission_required = 'ferias_binacionales.delete_expedicionacta'
    model = ExpedicionActa
    success_url = reverse_lazy('ferias_binacionales:expedicion_acta')



# ----------------------------- Doble Nacional ---------------------------------
class DobleNacionalidadList(PermissionRequiredMixin,ListView):
    permission_required = 'ferias_binacionales.view_doblenacionalidad'
    model = DobleNacionalidad
    template_name = 'ferias_binacionales/doble_nacionalidad/doble_nacionalidad_list.html'

class NuevaDobleNacionalidad(PermissionRequiredMixin,CreateView):
    permission_required = 'ferias_binacionales.add_doblenacionalidad'
    model = DobleNacionalidad
    form_class = DobleNacionalidadForm
    extra_context = {'editar': False, 'boton':"Guardar"}
    template_name = 'ferias_binacionales/doble_nacionalidad/doblenacionalidad_form.html'
    success_url = reverse_lazy('ferias_binacionales:doble_nacionalidad')  

class DetalleDobleNacionalidad(PermissionRequiredMixin,DetailView):
    permission_required = 'ferias_binacionales.view_doblenacionalidad'
    model = DobleNacionalidad
    context_object_name = 'nacionalidad'
    template_name = 'ferias_binacionales/doble_nacionalidad/doble_nacionalidad_detail.html'

class ActualizarDobleNacionalidad(PermissionRequiredMixin,UpdateView):
    permission_required = 'ferias_binacionales.change_doblenacionalidad'
    model = DobleNacionalidad
    form_class = DobleNacionalidadForm
    extra_context = {'editar': True, 'boton':"Actualizar"}
    template_name = 'ferias_binacionales/doble_nacionalidad/doblenacionalidad_form.html'
    success_url = reverse_lazy('ferias_binacionales:doble_nacionalidad')  

class EliminarDobleNacionalidad(PermissionRequiredMixin, DeleteView):
    permission_required = 'ferias_binacionales.delete_doblenacionalidad'
    model = DobleNacionalidad
    success_url = reverse_lazy('ferias_binacionales:doble_nacionalidad')  


# ----------------------------- Corrección de Acta de Nacimiento ---------------------------------
class CorreccionActaList(PermissionRequiredMixin, ListView):
    permission_required = 'ferias_binacionales.view_correccionacta'
    model = CorreccionActa
    template_name = 'ferias_binacionales/correccion_acta/correccion_acta_list.html'

class NuevaCorreccionActa(PermissionRequiredMixin, CreateView):
    permission_required = 'ferias_binacionales.add_correccionacta'
    model = CorreccionActa
    form_class = CorreccionActaForm
    extra_context = {'editar': False, 'boton':"Guardar"}
    template_name = 'ferias_binacionales/correccion_acta/correccionacta_form.html'
    success_url = reverse_lazy('ferias_binacionales:correccion_acta')

class DetalleCorreccionActa(PermissionRequiredMixin, DetailView):
    permission_required = 'ferias_binacionales.view_correccionacta'
    model = CorreccionActa
    context_object_name = 'correccion'
    template_name = 'ferias_binacionales/correccion_acta/correccion_acta_detail.html'

class ActualizarCorreccionActa(PermissionRequiredMixin,UpdateView):
    permission_required = 'ferias_binacionales.change_correccionacta'
    model = CorreccionActa
    form_class = CorreccionActaForm
    extra_context = {'editar': True, 'boton':"Actualizar"}
    template_name = 'ferias_binacionales/correccion_acta/correccionacta_form.html'
    success_url = reverse_lazy('ferias_binacionales:correccion_acta') 

class EliminarCorreccionActa(PermissionRequiredMixin, DeleteView):
    permission_required = 'ferias_binacionales.delete_correccionacta'
    model = CorreccionActa
    success_url = reverse_lazy('ferias_binacionales:correccion_acta') 
      
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

class ActualizarMandamientosJudiciales(PermissionRequiredMixin,UpdateView):
    permission_required = 'ferias_binacionales.change_mandamientosjudiciales'
    model = MandamientosJudiciales
    form_class = MandamientosJudicialesForm
    extra_context = {'editar': True, 'boton':"Actualizar"}
    success_url = reverse_lazy('ferias_binacionales:mandamiento_judicial')  
    template_name = 'ferias_binacionales/mandamientos_judiciales/mandamientosjudiciales_form.html'

class EliminarMandamientosJudiciales(PermissionRequiredMixin, DeleteView):
    permission_required = 'ferias_binacionales.delete_mandamientosjudiciales'
    model = MandamientosJudiciales
    success_url = reverse_lazy('ferias_binacionales:mandamiento_judicial')  