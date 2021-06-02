from django.urls import path
from . import views

app_name = 'consultas'

urlpatterns = [
    path('', views.index, name='index'),
    path('consulta/', views.consulta, name='consulta'),
    path('detalle/', views.detalle, name='detalle'),
]