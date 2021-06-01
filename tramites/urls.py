from django.urls import path
# Se importan las vistas a llamar en esta aplicación
# del proyecto 
from . import views

app_name = 'tramites'

urlpatterns = [
    path('lista/',views.TramiteList.as_view(), name = 'lista_tramite'),
    path('pedir-curp',views.pedir_curp,name='pedir_curp'),
]

