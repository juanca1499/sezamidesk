from django import forms 
from .models import Apostilla
from django.contrib.auth.forms import UserCreationForm

class ApostillaForm(forms.ModelForm):   
    class Meta:
        model = Apostilla
        fields = ('acta_americana','acta_mexicana','identificacion_padres','curp','comprobante_domicilio','rfc')
        widgets = {                   
            # Propios de la apostilla            
            'acta_americana':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'acta_mexicana':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'identificacion_padres':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'curp':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'comprobante_domicilio':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'rfc':forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }