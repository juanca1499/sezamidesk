from django.urls import path
from . import views

app_name = 'beneficiarios'

urlpatterns = [
    path('', views.BeneficiariosPrincipal.as_view(), name = 'principal'),
]