from django.shortcuts import render
from .models import Tramite
from django.views.generic import ListView
from django.contrib.auth.mixins import PermissionRequiredMixin


class TramiteList(ListView):
    model = Tramite
    template_name= 'tramites/tramite_list.html'

    #def get(self, request, *args, **kwargs):
    #    lista_grupos = Tramite.objects.all()
