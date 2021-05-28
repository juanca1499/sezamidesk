from django import forms
from django.contrib.auth.models import Group
from .models import Empleado 

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        
        fields = ('first_name','last_name','segundo_apellido','alias','telefono','username','password','grupo')

        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre(s)','onFocus':'validar(this)'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Primer apellido','onFocus':'validar(this)'}),
            'segundo_apellido':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Segundo apellido','onFocus':'validar(this)'}),
            'alias':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Alias','onFocus':'validar(this)'}),
            'telefono':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Teléfono','pattern':'[0-9]+'}),
            'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de usuario','onFocus':'validar(this)'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Contraseña'}),
            'grupo':forms.Select(attrs={'class':'form-control'}),
        }

    def save(self, commit=True):
        user = super(EmpleadoForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
