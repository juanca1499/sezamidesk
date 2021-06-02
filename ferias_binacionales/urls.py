from django.urls import path
# Se importan las vistas a llamar en esta aplicación
# del proyecto 
from . import views

app_name = 'ferias_binacionales'

urlpatterns = [
    path('servicios/',views.servicios,name='servicios'),

    path('constancia-estudios/',views.ConstanciaEstudioList.as_view(),name='constancia_estudios'),
    path('constancia-estudios/nuevo/',views.NuevaConstanciaEstudio.as_view(),name='nuevo_constancia_estudios'),
    path('constancia-estudios/detalle/<str:pk>',views.DetalleConstanciaEstudio.as_view(),name='detalle_constancia_estudios'),
    path('constancia-estudios/editar/<str:pk>',views.ActualizarConstanciaEstudio.as_view(),name='actualizar_constancia_estudios'),
    path('constancia-estudios/eliminar/<str:pk>',views.EliminarConstanciaEstudio.as_view(),name='eliminar_constancia_estudios'),


    path('defensoria-publica/',views.DefensoriaPublicaList.as_view(),name='defensoria_publica'),
    path('defensoria-publica/nuevo/',views.NuevaDefensoriaPublica.as_view(),name='nuevo_defensoria_publica'),
    path('defensoria-publica/detalle/<int:pk>',views.DetalleDefensoriaPublica.as_view(),name='detalle_defensoria_publica'),
    path('defensoria-publica/editar/<int:pk>',views.ActualizarDefensoriaPublica.as_view(),name='actualizar_defensoria_publica'),
    path('defensoria-publica/eliminar/<int:pk>',views.EliminarDefensoriaPublica.as_view(),name='eliminar_defensoria_publica'),


    path('licencia-conducir/',views.LicenciaConducirList.as_view(),name='licencia_conducir'),
    path('licencia-conducir/nuevo/',views.NuevaLicenciaConducir.as_view(),name='nuevo_licencia_conducir'),
    path('licencia-conducir/detalle/<int:pk>',views.DetalleLicenciaConducir.as_view(),name='detalle_licencia_conducir'),
    path('licencia-conducir/editar/<int:pk>',views.ActualizarLicenciaConducir.as_view(),name='actualizar_licencia_conducir'),
    path('licencia-conducir/eliminar/<int:pk>',views.EliminarLicenciaConducir.as_view(),name='eliminar_licencia_conducir'),


    path('expedicion-acta/',views.ExpedicionActaList.as_view(),name='expedicion_acta'),
    path('expedicion-acta/nuevo/',views.NuevaExpedicionActa.as_view(),name='nuevo_expedicion_acta'),
    path('expedicion-acta/detalle/<int:pk>',views.DetalleExpedicionActa.as_view(),name='detalle_expedicion_acta'),
    path('expedicion-acta/editar/<int:pk>',views.ActualizarExpedicionActa.as_view(),name='actualizar_expedicion_acta'),
    path('expedicion-acta/eliminar/<int:pk>',views.EliminarExpedicionActa.as_view(),name='eliminar_expedicion_acta'),

    path('doble-nacionalidad/',views.DobleNacionalidadList.as_view(),name='doble_nacionalidad'),
    path('doble-nacionalidad/nuevo/',views.NuevaDobleNacionalidad.as_view(),name='nuevo_doble_nacionalidad'),
    path('doble-nacionalidad/detalle/<int:pk>',views.DetalleDobleNacionalidad.as_view(),name='detalle_doble_nacionalidad'),
    path('doble-nacionalidad/editar/<int:pk>',views.ActualizarDobleNacionalidad.as_view(),name='actualizar_doble_nacionalidad'),
    path('doble-nacionalidad/eliminar/<int:pk>',views.EliminarDobleNacionalidad.as_view(),name='eliminar_doble_nacionalidad'),


    path('correccion-acta/',views.CorreccionActaList.as_view(),name='correccion_acta'),
    path('correccion-acta/nuevo/',views.NuevaCorreccionActa.as_view(),name='nuevo_correccion_acta'),
    path('correccion-acta/detalle/<int:pk>',views.DetalleCorreccionActa.as_view(),name='detalle_correccion_acta'),
    path('correccion-acta/editar/<int:pk>',views.ActualizarCorreccionActa.as_view(),name='actualizar_correccion_acta'),
    path('correccion-acta/eliminar/<int:pk>',views.EliminarCorreccionActa.as_view(),name='eliminar_correccion_acta'),

    path('mandamientos-judiciales/',views.MandamientosJudicialesList.as_view(),name='mandamiento_judicial'),
    path('mandamientos-judiciales/nuevo/',views.NuevaMandamientosJudiciales.as_view(),name='nuevo_mandamiento_judicial'),
    path('mandamientos-judiciales/detalle/<int:pk>',views.DetalleMandamientosJudiciales.as_view(),name='detalle_mandamiento_judicial'),
    path('mandamientos-judiciales/editar/<int:pk>',views.ActualizarMandamientosJudiciales.as_view(),name='actualizar_mandamiento_judicial'),
    path('mandamientos-judiciales/eliminar/<int:pk>',views.EliminarMandamientosJudiciales.as_view(),name='eliminar_mandamiento_judicial'),

]