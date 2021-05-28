from django.urls import path
from . import views

app_name = 'empleados'

urlpatterns = [
    path('lista/', views.EmpleadoList.as_view(), name='lista'),
    path('nuevo/', views.NuevoEmpleado.as_view(), name='nuevo'),
    path('permisos/<int:pk>', views.permisos, name='permisos'),
    path('agrega-permisos/<int:pk>', views.agregaPermiso, name='agrega-permisos'),
]