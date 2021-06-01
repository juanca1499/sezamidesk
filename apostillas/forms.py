from django import forms 
from .models import Apostilla
from django.contrib.auth.forms import UserCreationForm

class ApostillaForm(forms.ModelForm):   
    class Meta:
        model = Apostilla
        exclude = ('estado','fecha_inicio','fecha_fin')
        widgets = {
            'curp':forms.TextInput(attrs={'class':'form-control','placeholder':'CURP'}),
            'primer_apellido':forms.TextInput(attrs={'class':'form-control','placeholder':'Apellido paterno'}),
            'segundo_apellido':forms.TextInput(attrs={'class':'form-control','placeholder':'Apellido materno'}),
            'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre(s)'}),
            'identificacion':forms.Select(attrs={'class':'form-control'}),
            'beneficiario_colectivo':forms.CheckboxInput(attrs={'class':'form-check-input', 'id':'beneficiario_colectivo'}) ,

            'tipo_vialidad':forms.Select(attrs={'class':'form-control'}),
            'nombre_vialidad':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de la vialidad'}),
            'entre_vialidades':forms.TextInput(attrs={'class':'form-control','placeholder':'Entre vialidades'}),
            'numero_exterior':forms.NumberInput(attrs={'class':'form-control','placeholder':'Número exterior'}),
            'numero_interior':forms.NumberInput(attrs={'class':'form-control','placeholder':'Número interior'}),
            'asentamiento':forms.Select(attrs={'class':'form-control'}),
            'descripcion_ubicacion':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descripción de la ubicación'}),

            'estudio_socioeconomico':forms.CheckboxInput(attrs={'class':'form-check-input', 'id':'estudio_socioeconomico'}),
            'estado_civil':forms.Select(attrs={'class':'form-control'}),
            'jefe_familia':forms.CheckboxInput(attrs={'class':'form-check-input', 'id':'jefe_familia'}),
            'ocupacion':forms.Select(attrs={'class':'form-control'}),
            'ingreso_mensual':forms.Select(attrs={'class':'form-control'}),
            'integrantes_familia':forms.NumberInput(attrs={'class':'form-control','placeholder':'Número de integrantes de la familia'}),
            'dependientes_economicos':forms.NumberInput(attrs={'class':'form-control','placeholder':'Número de dependientes económicos'}),
            # tipo de vivienda???
            'vivienda':forms.Select(attrs={'class':'form-control'}),
            'numero_habitantes_vivienda':forms.NumberInput(attrs={'class':'form-control','placeholder':'Número de habitantes de la vivienda'}),
            'vivienda_electricidad':forms.CheckboxInput(attrs={'class':'form-check-input', 'id':'vivienda_electricidad'}),
            'vivienda_agua':forms.CheckboxInput(attrs={'class':'form-check-input', 'id':'vivienda_agua'}),
            'vivienda_drenaje':forms.CheckboxInput(attrs={'class':'form-check-input', 'id':'vivienda_drenaje'}),
            'vivienda_gas':forms.CheckboxInput(attrs={'class':'form-check-input', 'id':'vivienda_gas'}),
            'vivienda_telefono':forms.CheckboxInput(attrs={'class':'form-check-input', 'id':'vivienda_telefono'}),
            'vivienda_internet':forms.CheckboxInput(attrs={'class':'form-check-input', 'id':'vivienda_internet'}),
            'nivel_estudios':forms.Select(attrs={'class':'form-control'}),
            'tipo_seguridad_social':forms.Select(attrs={'class':'form-control'}),
            'discapacidad':forms.Select(attrs={'class':'form-control'}),
            'grupo_vulnerable':forms.Select(attrs={'class':'form-control'}),
                    
            # Propios de la apostilla            
            'acta_americana':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'acta_mexicana':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'identificacion_padres':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'curp':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'comprobante_domicilio':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'rfc':forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }