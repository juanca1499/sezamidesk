from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField 

class Empleado(User):
    segundo_apellido = models.CharField('Apellido materno',max_length=40,default=' ',null=False)
    alias = models.CharField('Alias',max_length=30,default=' ',null=False)
    telefono = models.CharField('Teléfono',max_length=15,null=True)
    grupo = models.ForeignKey("empleados.Grupo", verbose_name=("Grupo"), on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name+' '+self.last_name+' '+self.segundo_apellido

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

class Grupo(models.Model):
    grupo = models.CharField(max_length=50)

    def __str__(self):
        return self.grupo

    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'