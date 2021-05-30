from django.db import models
from django.core.validators import RegexValidator

class PersonaDesaparecida(models.Model):
    curp = models.CharField('CURP',primary_key=True,max_length=18,validators=[RegexValidator('([A-Z]{4}([0-9]{2})(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])[HM](AS|BC|BS|CC|CL|CM|CS|CH|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS|NE)[A-Z]{3}[0-9A-Z]\d)')])
    nombre_desaparecido = models.CharField('Nombre',max_length=50)
    apellido_paterno_desaparecido = models.CharField('Apellido paterno',max_length=50)
    apellido_materno_desaparecido = models.CharField('Apellido materno',max_length=50,blank=True, null=True)
    fecha_nacimiento_desaparecido = models.DateField('Fecha de nacimiento')
    observaciones = models.CharField('Observaciones',max_length=150)
    estatus = models.ForeignKey("localizacion_personas.Estatus",verbose_name='Estatus', on_delete=models.CASCADE)
    ultimo_lugar = models.CharField('Última lugar dónde se sabe al desaparecido(a)',max_length=30)
    fecha_desaparicion = models.DateField('Fecha de desaparición')
    telefono_solicitante = models.CharField("Teléfono",max_length=10,validators=[RegexValidator('^(\d{10})$')],blank=True, null=True)
    nombre_solicitante = models.CharField('Nombre',max_length=50)
    apellido_paterno_solicitante = models.CharField('Apellido paterno',max_length=50)
    apellido_materno_solicitante = models.CharField('Apellido materno',max_length=50,blank=True, null=True)

    def __str__(self):
        return self.nombre_desaparecido
    
    class Meta:
        verbose_name = 'Persona desaparecida'
        verbose_name_plural = 'Personas desaparecidas'

class Estatus(models.Model):
    estatus = models.CharField(max_length=30)

    def __str__(self):
        return self.estatus
    class Meta:
        verbose_name = 'Estatus'
        verbose_name_plural = 'Estatus'