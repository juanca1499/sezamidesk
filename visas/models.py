from django.db import models
from django.core.validators import RegexValidator

class Visa(models.Model):
    curp = models.CharField("CURP", primary_key = True, max_length=18,
    validators=[RegexValidator('([A-Z]{4}([0-9]{2})(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])[HM](AS|BC|BS|CC|CL|CM|CS|CH|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS|NE)[A-Z]{3}[0-9A-Z]\d)')])
    primer_apellido = models.CharField("Primer apellido", max_length=50)
    segundo_apellido = models.CharField("Segundo apellido", max_length=50)
    nombre = models.CharField("Nombre(s)", max_length=50)
    pasaporte = models.BooleanField('Pasaporte',default=False)
    direccion_usa = models.CharField('Dirección de Estados Unidos',max_length=70)
    persona_visitar = models.CharField('Nombre de la persona a visitar',max_length=70)
    tel_persona_visitar = models.CharField('Teléfono de la persona a visitar',max_length=10)
    fe_nacimiento_madre = models.DateField('Fecha de nacimiento de la madre')
    fe_nacimiento_padre = models.DateField('Fecha de nacimiento del padre')
    dir_trabajo_escuela = models.CharField('Dirección del lugar de trabajo o escuela',max_length=80)
    nom_dir_trabajo_escuela = models.CharField('Nombre de la dirección del trabajo o escuela',max_length=35)
    fe_ingreso_trabajo_escuela = models.DateField('Fecha de ingreso al trabajo o escuela')
    ingreso_mensual = models.DecimalField('Ingreso Mensual',max_digits=10, decimal_places=2)
    fecha_viaje = models.DateField('Fecha tentativa de viaje')
    correo = models.EmailField('Correo electrónico')
    red_social = models.URLField('URL de la red social')
    pago = models.BooleanField(default=False)
    fecha_cita = models.DateField('Fecha de la cita en el consulado',null=True,blank=True)
    asesor = models.OneToOneField('empleados.Empleado',null=True, blank=True,on_delete=models.CASCADE)