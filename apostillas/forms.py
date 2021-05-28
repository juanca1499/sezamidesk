from django import forms 
from .models import Apostilla
from django.contrib.auth.forms import UserCreationForm

class ApostillaForm(forms.ModelForm):
    
    class Meta:
        model = Apostilla
        fields = '__all__'