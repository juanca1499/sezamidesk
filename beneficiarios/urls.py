from django.urls import path
from . import views

app_name = 'beneficiarios'

urlpatterns = [
    path('', views.BeneficiariosPrincipal.as_view(), name = 'principal'),
    path('detalle/<str:pk>', views.BeneficiariosDetalle.as_view(), name = 'detalle'),
    path('editar/<str:pk>', views.BeneficiariosEditar.as_view(), name = 'editar'),
    path('eliminar/<str:pk>', views.BeneficiariosEliminar.as_view(), name = 'eliminar'),
]