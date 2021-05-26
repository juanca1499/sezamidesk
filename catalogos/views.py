from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.conf import settings

# Create your views here.
class CatalogoGeneral(TemplateView):
    template_name = 'base.html'
