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
    beneficiario = get_object_or_404(Beneficiario,curp=curp)
    tramite = get_object_or_404(Tramite,beneficiario=beneficiario)
    return render(request, 'detalle.html',{'beneficiario':beneficiario,
                                            'tramite':tramite,})