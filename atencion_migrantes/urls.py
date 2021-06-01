from django.urls import path
from . import views

app_name = 'atencion_migrantes'

urlpatterns = [
    path('', views.AtencionMigrantesPrincipal.as_view(), name = 'principal'),
    path("detalle/<int:pk>", views.AtencionMigrantesDetalle.as_view(), name="detalle"),
    path("eliminar/<int:pk>", views.AtencionMigrantesEliminar.as_view(), name="eliminar"),
]