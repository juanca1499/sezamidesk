from django.contrib.auth.models import Group
from django.urls.base import reverse
from empleados.models import Empleado,Grupo
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.models import Group

from .forms import EmpleadoForm
from .models import Empleado

# Create your views here.

class EmpleadoList(ListView):
    model = Empleado   

class NuevoEmpleado(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    extra_context = {'etiqueta':'Nuevo','btn':'Agregar'} 
    def get_success_url(self):
        return reverse('empleados:permisos',args=(self.object.id,))

    def form_valid(self, form):
        user = form.save(commit=False)
        return super().form_valid(form)

def permisos(request, pk):
    empleado = get_object_or_404(Empleado,pk=pk)
    grupo = get_object_or_404(Grupo,grupo=empleado.grupo)
    groups = Group.objects.all()
    permisos=[]
    for group in groups:
        p = group.name.split(" ")
        if(grupo.grupo==p[0]):
            permisos.append(group)
    return render(request, 'lista_permisos.html',{'permisos':permisos,
                                                   'grupo':grupo,
                                                   'empleado':empleado})

def agregaPermiso(request, pk):
    empleado = Empleado.objects.get(id=pk)
    grupos = [grupo.id for grupo in Group.objects.all()]

    if len(request.POST) > 1: 
        empleado.groups.clear()
        for item in request.POST:
            if request.POST[item] == 'on':
                empleado.groups.add(Group.objects.get(id=int(item)))
    return redirect('empleados:lista')

