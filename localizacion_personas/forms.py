from django import forms
from .models import PersonaDesaparecida
from django.core.validators import RegexValidator

class DateInput(forms.DateInput):
    input_type = 'date'

class PersonaDesaparecidaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PersonaDesaparecidaForm, self).__init__(*args, **kwargs)
        self.fields['estatus'].initial = 1

    fecha_nacimiento_desaparecido = forms.DateField(widget=DateInput())
    fecha_desaparicion = forms.DateField(widget=DateInput())
    class Meta:
        model = PersonaDesaparecida
        fields = '__all__'
        widgets = {
                'folio':forms.HiddenInput(attrs={'class':'form-control','placeholder':'Folio'}),
                'nombre_desaparecido':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}),
                'apellido_paterno_desaparecido':forms.TextInput(attrs={'class':'form-control','placeholder':'Apellido paterno'}),
                'apellido_materno_desaparecido':forms.TextInput(attrs={'class':'form-control','placeholder':'Apellido materno'}),
                'fecha_nacimiento_desaparecido':forms.DateInput(attrs={'class':'form-control','placeholder':'Fecha de nacimiento'}),
                'observaciones':forms.Textarea(attrs={'class':'form-control','placeholder':'Observaciones','rows':4}),
                'estatus':forms.Select(attrs={'class':'form-select'}),
                'ultimo_lugar':forms.TextInput(attrs={'class':'form-control','placeholder':'Último lugar dónde se sabe al desaparecido(a)'}),
                'fecha_desaparicion':forms.DateInput(attrs={'class':'form-control'}),
                'telefono_solicitante':forms.TextInput(attrs={'class':'form-control','placeholder':'Número de télefono del solicitante'}),
                'nombre_solicitante':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre del solicitante'}),
                'apellido_paterno_solicitante':forms.TextInput(attrs={'class':'form-control','placeholder':'Apellido paterno del solicitante'}),
                'apellido_materno_solicitante':forms.TextInput(attrs={'class':'form-control','placeholder':'Apellido materno del solicitante'}),
        }