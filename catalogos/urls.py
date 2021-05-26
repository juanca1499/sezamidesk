from django.urls import path
# Se importan las vistas a llamar en esta aplicación
# del proyecto 
from . import views

app_name = 'catalogos'

urlpatterns = [
    path('index/', views.CatalogoGeneral.as_view(), name = 'index')
]

