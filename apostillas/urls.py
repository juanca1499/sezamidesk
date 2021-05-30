from django.urls import path
from . import views

app_name = 'apostillas'

urlpatterns = [
    path('',views.ListaApostilla.as_view(),name='lista'),
    path('nueva/',views.NuevaApostilla.as_view(),name='nueva'),
    path('detalle/<int:pk>',views.DetalleApostilla.as_view(),name='detalle'),
    path('editar/<int:pk>',views.EditarApostilla.as_view(),name='editar'),
    path('eliminar/<int:pk>',views.EliminarApostilla.as_view(),name='eliminar')
]