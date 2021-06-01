from django import forms 

class PedirCurpForm(forms.Form):
    curp = forms.CharField(label='Indica la CURP del beneficiario',max_length=18)

    class Meta:
        widgets = {
            'curp':forms.TextInput(attrs={'class':'form-control','placeholder':'Indica tu CURP'})
        }