from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('catalogos.urls')),
    path('apostillas/',include('apostillas.urls')),
    path('tramites/',include('tramites.urls')),
    path('beneficiarios/', include('beneficiarios.urls')),
    path('empleados/',include('empleados.urls')),
    path('localizacion-personas/',include('localizacion_personas.urls')),
    path('atencion-migrantes/',include('atencion_migrantes.urls')),
]
