from django import forms 
from .models import Apostilla
from django.contrib.auth.forms import UserCreationForm

from beneficiarios.forms import BeneficiarioForm

class ApostillaForm(BeneficiarioForm,forms.ModelForm):   
    class Meta:
        model = Apostilla
        exclude = ('estado','fecha_inicio','fecha_fin')
        widgets = {                   
            # Propios de la apostilla            
            'acta_americana':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'acta_mexicana':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'identificacion_padres':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'curp':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'comprobante_domicilio':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'rfc':forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }