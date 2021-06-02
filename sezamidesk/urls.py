from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('consultas.urls')),
    path('apostillas/',include('apostillas.urls')),
    path('tramites/',include('tramites.urls')),
    path('beneficiarios/', include('beneficiarios.urls')),
    path('empleados/',include('empleados.urls')),
    path('localizacion-personas/',include('localizacion_personas.urls')),
    path('atencion-migrantes/',include('atencion_migrantes.urls')),
    path('ferias-binacionales/',include('ferias_binacionales.urls')),
    path('visas/',include('visas.urls')),
]
