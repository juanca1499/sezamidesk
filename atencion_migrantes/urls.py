from django.urls import path
from . import views

app_name = 'atencion_migrantes'

urlpatterns = [
    path('', views.AtencionMigrantesPrincipal.as_view(), name = 'principal'),
]