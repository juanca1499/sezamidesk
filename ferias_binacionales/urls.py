from django.urls import path
# Se importan las vistas a llamar en esta aplicación
# del proyecto 
from . import views

app_name = 'ferias_binacionales'

urlpatterns = [
    path('servicios/',views.servicios,name='servicios'),

    path('constancia-estudios/',views.ConstanciaEstudioList.as_view(),name='constancia_estudios'),
    path('constancia-estudios/nuevo/',views.NuevaConstanciaEstudio.as_view(),name='nuevo_constancia_estudios'),

    path('defensoria-publica/',views.DefensoriaPublicaList.as_view(),name='defensoria_publica'),
    path('defensoria-publica/nuevo/',views.NuevaDefensoriaPublica.as_view(),name='nuevo_defensoria_publica'),

    path('licencia-conducir/',views.LicenciaConducirList.as_view(),name='licencia_conducir'),
    path('licencia-conducir/nuevo/',views.NuevaLicenciaConducir.as_view(),name='nuevo_licencia_conducir'),

    path('expedicion-acta/',views.ExpedicionActaList.as_view(),name='expedicion_acta'),
    path('expedicion-acta/nuevo/',views.NuevaExpedicionActa.as_view(),name='nuevo_expedicion-acta'),

    path('doble-nacionalidad/',views.DobleNacionalidadList.as_view(),name='doble_nacionalidad'),
    path('doble-nacionalidad/nuevo/',views.NuevaDobleNacionalidad.as_view(),name='nuevo_doble_nacionalidad'),

    path('correccion-acta/',views.CorreccionActaList.as_view(),name='correccion_acta'),
    path('correccion-acta/nuevo/',views.NuevaCorreccionActa.as_view(),name='nuevo_correccion_acta'),

    path('mandamientos-judiciales/',views.MandamientosJudicialesList.as_view(),name='mandamiento_judicial'),
    path('mandamientos-judiciales/nuevo/',views.NuevaMandamientosJudiciales.as_view(),name='nuevo_mandamiento_judicial'),
]