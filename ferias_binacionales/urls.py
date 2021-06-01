from django.urls import path
# Se importan las vistas a llamar en esta aplicación
# del proyecto 
from . import views

app_name = 'ferias_binacionales'

urlpatterns = [
    path('servicios/',views.servicios,name='servicios'),
    path('constancia-estudios/',views.ConstanciaEstudioList.as_view(),name='constancia_estudios'),
    path('defensoria-publica/',views.DefensoriaPublicaList.as_view(),name='defensoria_publica'),
    path('licencia-conducir/',views.LicenciaConducirList.as_view(),name='licencia_conducir'),
    path('expedicion-acta/',views.ExpedicionActaList.as_view(),name='expedicion_acta'),
    path('doble-nacionalidad/',views.DobleNacionalidadList.as_view(),name='doble_nacionalidad'),
    path('correcion-acta/',views.CorreccionActaList.as_view(),name='correcion_acta'),
    path('mandamientos-judiciales/',views.MandamientosJudicialesList.as_view(),name='mandamiento_judicial'),
]