from django.db import models
from django.core.validators import RegexValidator

class Visa(models.Model):
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
    pago = models.BooleanField(default=False)
    fecha_cita = models.DateField('Fecha de la cita en el consulado',null=True,blank=True)
    tramite = models.ForeignKey('tramites.Tramite',verbose_name='Trámite',on_delete=models.CASCADE)

class VisaRedSocial(models.Model):
    visa = models.ForeignKey('visas.Visa',verbose_name='Trámite de visa', on_delete=models.CASCADE)
    red_social = models.URLField('URL de la red social')