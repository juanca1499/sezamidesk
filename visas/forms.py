from django import forms 
from .models import Visa
from django.contrib.auth.forms import UserCreationForm

class DateInput(forms.DateInput):
    input_type = 'date'

class VisaForm(forms.ModelForm):
    fe_nacimiento_madre = forms.DateField(widget=DateInput())
    fe_nacimiento_padre = forms.DateField(widget=DateInput())    
    fe_ingreso_trabajo_escuela = forms.DateField(widget=DateInput())
    fecha_viaje = forms.DateField(widget=DateInput())
    fecha_cita = forms.DateField(widget=DateInput())

    class Meta:
        model = Visa
        exclude = ('asesor',)

        widgets = {
            'curp':forms.TextInput(attrs={'class':'form-control','placeholder':'CURP'}),
            'direccion_usa':forms.TextInput(attrs={'class':'form-control','placeholder':'Dirección en Estados Unidos'}),
            'persona_visitar':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre de la persona a visitar'}),
            'tel_persona_visitar':forms.TextInput(attrs={'class':'form-control','placeholder':'Teléfono de la persona a visitar'}),
            'fe_nacimiento_madre':forms.DateInput(attrs={'class':'form-control','placeholder':'Fecha de nacimiento de la madre'}),
            'fe_nacimiento_padre':forms.DateInput(attrs={'class':'form-control','placeholder':'Fecha de nacimiento del padre'}),
            'dir_trabajo_escuela':forms.TextInput(attrs={'class':'form-control','placeholder':'Dirección del lugar de trabajo o escuela'}),
            'nom_dir_trabajo_escuela':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre del lugar de trabajo o escuela'}),
            'fe_ingreso_trabajo_escuela':forms.DateInput(attrs={'class':'form-control','placeholder':'Fecha de ingreso al trabajo o escuela'}),
            'fecha_viaje':forms.DateInput(attrs={'class':'form-control'}),
            'correo':forms.EmailInput(attrs={'class':'form-control'}),
            'url':forms.URLField(),
            'pasaporte':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'pago':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'fecha_cita':forms.DateInput(attrs={'class':'form-control','placeholder':'Fecha de la cita en el consulado'}),
        }