from django import forms
from .models import PersonaDesaparecida
from django.core.validators import RegexValidator

class DateInput(forms.DateInput):
    input_type = 'date'

class PersonaDesaparecidaForm(forms.ModelForm):
    fecha_nacimiento_desaparecido = forms.DateField(widget=DateInput())
    class Meta:
        model = PersonaDesaparecida
        fields = '__all__'
        widgets = {
                'curp':forms.TextInput(attrs={'class':'form-control','onFocus':'validar(this)'}),
                'nombre_desaparecido':forms.TextInput(attrs={'class':'form-control'}),
                'apellido_paterno_desaparecido':forms.TextInput(attrs={'class':'form-control'}),
                'apellido_materno_desaparecido':forms.TextInput(attrs={'class':'form-control'}),
                'fecha_nacimiento_desaparecido':forms.DateInput(attrs={'class':'form-control'}),
                'observaciones':forms.Textarea(attrs={'class':'form-control'}),
                'estatus':forms.TextInput(attrs={'class':'form-control'}),
                'ultimo_lugar':forms.TextInput(attrs={'class':'form-control'}),
                'fecha_desaparicion':forms.DateInput(attrs={'class':'form-control'}),
                'telefono_solicitante':forms.TextInput(attrs={'class':'form-control'}),
                'nombre_solicitante':forms.TextInput(attrs={'class':'form-control'}),
                'apellido_paterno_solicitante':forms.TextInput(attrs={'class':'form-control'}),
                'apellido_materno_solicitante':forms.TextInput(attrs={'class':'form-control'}),
        }