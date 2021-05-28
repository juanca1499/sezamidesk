from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Beneficiario

class BeneficiariosPrincipal(ListView):
    model = Beneficiario
    template_name = "beneficiarios_principal.html"

class BeneficiariosDetalle(DetailView):
    model = Beneficiario
