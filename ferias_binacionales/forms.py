from django import forms 
from .models import *
from django.contrib.auth.forms import UserCreationForm

class DateInput(forms.DateInput):
    input_type = 'date'

class ConstanciaEstudioForm(forms.ModelForm):   
    class Meta:
        model = ConstanciaEstudios
        fields = '__all__'
        widgets = {   
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre(s)','onFocus':'validar(this)'}),
            'ap_paterno': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido Paterno'}),
            'ap_materno': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido Materno'}),
            'curp':forms.TextInput(attrs={'class':'form-control','placeholder':'CURP'}),
            'nivel_estudios':forms.Select(attrs={'class':'form-control','placeholder':'Nivel Estudios'}),
            'nombre_escuela':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre Escuela'}),
            'localidad':forms.Select(attrs={'class':'form-control','placeholder':'Localidad'}),
            'anio_aprox':forms.NumberInput(attrs={'class':'form-control','placeholder':'Año'}),
            'fotografia':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'num_telefonico':forms.TextInput(attrs={'class':'form-control','placeholder':'Número telefónico'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Correo Electrónico'}),
        }

class DefensoriaPublicaForm(forms.ModelForm):   
    fecha = forms.DateField(widget=DateInput())
    class Meta:
        model = DefensoriaPublica
        fields = '__all__'
        widgets = {   
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre(s)','onFocus':'validar(this)'}),
            'ap_paterno': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido Paterno'}),
            'ap_materno': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido Materno'}),
            'tramite_realizar': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Trámite a realizar'}),
            'fecha':forms.DateInput(attrs={'class':'form-control'}),
            'localidad':forms.Select(attrs={'class':'form-control','placeholder':'Localidad'}),
            'num_telefonico':forms.TextInput(attrs={'class':'form-control','placeholder':'Número telefónico'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Correo Electrónico'}),
        }

class LicenciaConducirForm(forms.ModelForm):  
    class Meta:
        model = LicenciaConducir
        fields = '__all__'
        widgets = {   
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre(s)','onFocus':'validar(this)'}),
            'ap_paterno': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido Paterno'}),
            'ap_materno': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido Materno'}),
            'acta_nacimiento':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'comprobante_dom_eeuu':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'referencia_dom_zac':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'fotografia':forms.CheckboxInput(attrs={'class':'form-check-input'}),          
            'tipo_sangre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tipo de Sangre'}),
            'identificacion_oficial':forms.CheckboxInput(attrs={'class':'form-check-input'}),          
            'estatus':forms.Select(attrs={'class':'form-control','placeholder':'Estatús del trámite'}),
        }


class ExpedicionActaForm(forms.ModelForm):   
    fecha_nacimiento = forms.DateField(widget=DateInput())
    class Meta:
        model = ExpedicionActa
        fields = '__all__'
        widgets = {   
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre(s)','onFocus':'validar(this)'}),
            'ap_paterno': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido Paterno'}),
            'ap_materno': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido Materno'}),   
            'nombre_solicitante': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre completo del solicitante'}),
            'fecha_nacimiento':forms.DateInput(attrs={'class':'form-control'}),
            'municipio_registro': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Municipio de registro'}),
        }
        
class DobleNacionalidadForm(forms.ModelForm):   
    class Meta:
        model = DobleNacionalidad
        fields = '__all__'
        widgets = {   
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre(s)','onFocus':'validar(this)'}),
            'ap_paterno': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido Paterno'}),
            'ap_materno': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido Materno'}),   
            'acta_nacimiento_original':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'actas_apostilladas':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'comprobante_domicilio':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'identificacion_oficial':forms.CheckboxInput(attrs={'class':'form-check-input'}),          
            'original_copias': forms.CheckboxInput(attrs={'class':'form-check-input'}),  
        } 

class CorreccionActaForm(forms.ModelForm):   
    class Meta:
        model = CorreccionActa
        fields = '__all__'
        widgets = {   
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre(s)','onFocus':'validar(this)'}),
            'ap_paterno': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido Paterno'}),
            'ap_materno': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido Materno'}),   
            'acta_a_corregir':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'documentos_comprobantes':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'testimonial':forms.CheckboxInput(attrs={'class':'form-check-input'}),          
            'solicitud_firmado': forms.CheckboxInput(attrs={'class':'form-check-input'}),  
            'original_copias': forms.CheckboxInput(attrs={'class':'form-check-input'}),  
        }        

class MandamientosJudicialesForm(forms.ModelForm):   
    fecha_nacimiento = forms.DateField(widget=DateInput())
    class Meta:
        model = MandamientosJudiciales
        fields = '__all__'
        widgets = {   
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre(s)','onFocus':'validar(this)'}),
            'ap_paterno': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido Paterno'}),
            'ap_materno': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido Materno'}),   
            'acta_nac_original':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'curp_act':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'comprobante_domicilio':forms.CheckboxInput(attrs={'class':'form-check-input'}),          
            'pasaporte_vigente': forms.CheckboxInput(attrs={'class':'form-check-input'}),  
            'matricula_consular': forms.CheckboxInput(attrs={'class':'form-check-input'}),  
            'pago_en_caja_fiscalia':forms.CheckboxInput(attrs={'class':'form-check-input'}),          
            'fotografia': forms.CheckboxInput(attrs={'class':'form-check-input'}),  
            'ine_familiar': forms.CheckboxInput(attrs={'class':'form-check-input'}),  
        }