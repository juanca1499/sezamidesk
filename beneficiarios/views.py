from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView


class BeneficiariosPrincipal(TemplateView):
    template_name = "beneficiarios_principal.html"
