from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Beneficiario
from .forms import BeneficiarioForm, BeneficiarioDireccionForm, EstudioSocioeconomicoForm
from django.urls import reverse_lazy


class BeneficiariosPrincipal(ListView):
    model = Beneficiario
    template_name = "beneficiarios_principal.html"

class BeneficiariosDetalle(DetailView):
    model = Beneficiario
    

class BeneficiariosEditar(UpdateView):
    model = Beneficiario
    form_class = BeneficiarioForm
    form_direccion = BeneficiarioDireccionForm
    form_estudio = EstudioSocioeconomicoForm

    extra_context = {
        'etiqueta':'Actualizar datos del',
        'boton':'Guardar',
        'form_direccion':form_direccion,
        'form_estudio':form_estudio,
    }
    success_url = reverse_lazy('beneficiarios:principal')

class BeneficiariosCrear(CreateView):
    model = Beneficiario
    form_class = BeneficiarioForm
    form_direccion = BeneficiarioDireccionForm
    form_estudio = EstudioSocioeconomicoForm
    extra_context = {
        'etiqueta':'Registrar nuevo',
        'boton':'Guardar',
        'form_direccion':form_direccion,
        'form_estudio':form_estudio,
    }
    success_url = reverse_lazy('beneficiarios:principal')

    def post(self,request,*args,**kwargs):
        form_beneficiario = BeneficiarioForm(request.POST)
        form_direccion = BeneficiarioDireccionForm(request.POST)

        form_estudio = EstudioSocioeconomicoForm(request.POST)

        if form_beneficiario.is_valid() and form_direccion.is_valid() and form_estudio.is_valid():
            estudio = form_estudio.save()
            direccion = form_direccion.save()
            beneficiario = form_beneficiario.save()
            beneficiario.direccion_id = direccion.id
            beneficiario.estudio_socioeconomico_id = estudio.id
            # direccion.save()
            # estudio.save()
            # Revisar si es necesario hacer save a dirección y estudio.
            beneficiario.save()
            return redirect('beneficiarios:principal')
         

class BeneficiariosEliminar(DeleteView):
    model = Beneficiario
    success_url = reverse_lazy('beneficiarios:principal')


def nueva_direccion(request):
    if request.method == "POST":
        form = BeneficiarioDireccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria:lista')

def nuevo_estudio(request):
    if request.method == "POST":
        form = BeneficiarioDireccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria:lista')
