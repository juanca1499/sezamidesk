from django.urls import path
from . import views

app_name = 'visas'

urlpatterns = [
    path('',views.ListaVisa.as_view(),name='lista'),
    path('nueva/',views.NuevaVisa.as_view(),name='nueva'),
    path('detalle/<slug:pk>',views.DetalleVisa.as_view(),name='detalle'),
    path('editar/<slug:pk>',views.EditarVisa.as_view(),name='editar'),
    path('eliminar/<slug:pk>',views.EliminarVisa.as_view(),name='eliminar'),
]