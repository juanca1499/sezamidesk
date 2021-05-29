from django.contrib.auth.models import Group
from django.urls.base import reverse
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView,UpdateView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.models import Group

from empleados.models import Empleado,Grupo
from .forms import EmpleadoForm,EmpleadoModificarForm
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

class EliminarEmpleado(DeleteView):
    model = Empleado
    success_url=reverse_lazy('empleado:lista')

class ModificarEmpleado(UpdateView):
    model = Empleado
    form_class = EmpleadoModificarForm
    extra_context = {'etiqueta':'Modificar','btn':'Guardar'} 

def permisos(request, pk):
    empleado = get_object_or_404(Empleado,pk=pk)
    grupo = get_object_or_404(Grupo,grupo=empleado.grupo)
    groups = Group.objects.all()
    grupos_empleado = empleado.groups.all()
    permisos=[]
    for group in groups:
        p = group.name.split(" ")
        if(grupo.grupo==p[0]):
            permisos.append(group)
    return render(request, 'lista_permisos.html',{'permisos':permisos,
                                                   'grupo':grupo,
                                                   'empleado':empleado,
                                                   'grupos_empleado':grupos_empleado})

def agregaPermiso(request, pk):
    empleado = Empleado.objects.get(id=pk)
    grupo_id=int(request.POST['grupo'])
    grupo = Grupo.objects.get(id=grupo_id)
    empleado.grupo=grupo
    empleado.save()
    empleado.groups.clear()
    for item in request.POST:
        if request.POST[item] == 'on':
            empleado.groups.add(Group.objects.get(id=int(item)))

    return redirect('empleados:lista')

def detalleEmpleado(request,pk):
    empleado = get_object_or_404(Empleado,pk=pk)
    grupos = empleado.groups.all()
    
    return render(request, 'empleado_detail.html',{'permisos':grupos,
                                                   'empleado':empleado})
                                                
def seleccionaGrupo(request,pk):
    empleado = get_object_or_404(Empleado,pk=pk)
    grupos = Grupo.objects.all()

    return render(request, 'empleado_grupo.html',{'grupos':grupos,
                                                   'empleado':empleado})

def seleccionarPermisos(request):
    empleado=Empleado.objects.get(pk=int(request.POST['empleado']))
    id_grupo=int(request.POST['select'])
    grupos_empleado = empleado.groups.all()
    grupo = Grupo.objects.get(id=id_grupo)
    groups = Group.objects.all()
    permisos=[]
    for group in groups:
        p = group.name.split(" ")
        if(grupo.grupo==p[0]):
            permisos.append(group)
    return render(request, 'lista_permisos.html',{'permisos':permisos,
                                                   'grupo':grupo,
                                                   'empleado':empleado,
                                                   'grupos_empleado':grupos_empleado,
                                                   'modificar':1})
