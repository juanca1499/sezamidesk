from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.urls.base import reverse
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView,UpdateView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

from empleados.models import Empleado,Grupo
from .forms import EmpleadoForm,EmpleadoModificarForm
from .models import Empleado

# Create your views here.

class EmpleadoList(PermissionRequiredMixin,ListView):
    permission_required = 'empleados.view_empleado'
    model = Empleado   

class NuevoEmpleado(PermissionRequiredMixin,CreateView):
    permission_required = 'empleados.add_empleado'
    model = Empleado
    form_class = EmpleadoForm
    extra_context = {'etiqueta':'Nuevo','btn':'Agregar'} 
    def get_success_url(self):
        return reverse('empleados:permisos',args=(self.object.id,))

    def form_valid(self, form):
        user = form.save(commit=False)
        return super().form_valid(form)

class EliminarEmpleado(PermissionRequiredMixin,DeleteView):
    permission_required = 'empleados.delete_empleado'
    model = Empleado
    success_url=reverse_lazy('empleados:lista')

class ModificarEmpleado(PermissionRequiredMixin,UpdateView):
    permission_required = 'empleados.change_empleado'
    model = Empleado
    form_class = EmpleadoModificarForm
    extra_context = {'etiqueta':'Modificar','btn':'Guardar'}
    success_url = reverse_lazy('empleados:lista') 

class EmpleadoLogin(LoginView):
    template_name='login.html'
    form_class = AuthenticationForm

class EmpleadoLogout(LogoutView):
    template_name='login.html'

@login_required
def verPerfil(request):
    empleado = get_object_or_404(Empleado,pk=request.user.id)
    permisos = empleado.groups.all()
    grupo = get_object_or_404(Grupo,grupo=empleado.grupo)
    admin ='El empleado es super administrador'

    if (grupo.grupo == "Super Admin"):
        return render(request, 'perfil.html',{'permisos':permisos,
                                            'empleado':empleado,
                                            'admin':admin})    

    return render(request, 'perfil.html',{'permisos':permisos,
                                            'empleado':empleado,})

@login_required
@permission_required('empleados.add_empleado', raise_exception=True)
def permisos(request, pk):
    empleado = get_object_or_404(Empleado,pk=pk)
    grupo = get_object_or_404(Grupo,grupo=empleado.grupo)

    if (grupo.grupo=="Super Admin"):
        guardarSuperAdmin(empleado,grupo)
        return redirect('empleados:lista')
    
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

@login_required
@permission_required('empleados.view_empleado', raise_exception=True)
def detalleEmpleado(request,pk):
    empleado = get_object_or_404(Empleado,pk=pk)
    grupos = empleado.groups.all()
    admin ='El empleado es super administrador'
    for grupo in grupos:
        if (grupo.name=='Super Admin'):
            return render(request, 'empleado_detail.html',{'permisos':grupos,
                                                           'empleado':empleado,
                                                           'admin':admin})
    
    return render(request, 'empleado_detail.html',{'permisos':grupos,
                                                   'empleado':empleado})

@login_required
@permission_required('empleados.change_empleado', raise_exception=True)                                                
def seleccionaGrupo(request,pk):
    empleado = get_object_or_404(Empleado,pk=pk)
    grupos = Grupo.objects.all()

    return render(request, 'empleado_grupo.html',{'grupos':grupos,
                                                   'empleado':empleado})

@login_required
@permission_required('empleados.change_empleado', raise_exception=True)
def seleccionarPermisos(request):
    empleado=Empleado.objects.get(pk=int(request.POST['empleado']))
    id_grupo=int(request.POST['select'])
    grupo = Grupo.objects.get(id=id_grupo)

    if (grupo.grupo=="Super Admin"):
        guardarSuperAdmin(empleado,grupo)
        return redirect('empleados:lista')

    grupos_empleado = empleado.groups.all()
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

def guardarSuperAdmin(empleado,grupo):
    empleado.grupo=grupo
    empleado.save()
    empleado.groups.clear()
    empleado.groups.add(Group.objects.get(name=grupo.grupo))