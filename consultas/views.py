from django.shortcuts import render
from django.shortcuts import get_object_or_404

from tramites.models import Tramite
from beneficiarios.models import Beneficiario
# Create your views here.

def index(request):
    return render(request, 'index.html')

def consulta(request):
    return render(request, 'consulta.html')

def detalle(request):
    curp = request.POST['curp']
    try:
        beneficiario = Beneficiario.objects.get(curp=curp)
        tramite = Tramite.objects.get(beneficiario=beneficiario)
        return render(request, 'detalle.html',{'beneficiario':beneficiario,
                                               'tramite':tramite,})
    except:
        return render(request, 'detalle.html')