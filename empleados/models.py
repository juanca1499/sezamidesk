from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField 

class Empleado(User):
    segundo_apellido = models.CharField('Apellido materno',max_length=40,default='Segundo apellido',null=False)
    alias = models.CharField('Alias',max_length=30,default='alias',null=False)
    telefono = models.CharField('Teléfono',max_length=15,null=True)

    def __str__(self):
        return self.first_name+' '+self.last_name+' '+self.apellido_materno

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
