from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView


class AtencionMigrantesPrincipal(TemplateView):
    template_name = "atencion_migrantes_principal.html"
