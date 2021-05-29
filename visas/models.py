from django.db import models

class Visa(models.Model):
    pasaporte = models.BooleanField('Pasaporte',default=False)
    direccion_usa_visitar = models.ForeignKey('visas.DireccionEstadosUnidos',on_delete=models.CASCADE)
    nombre_persona_visitar = models.CharField('Nombre de la persona a visitar',max_length=70)
    telefono_persona_visitar = models.CharField('Teléfono de la persona a visitar',max_length=10)
    fecha_nacimiento_madre = models.DateField()
    fecha_nacimiento_padre = models.DateField()
    direccion_trabajo_escuela = models.CharField('Dirección del lugar de trabajo o escuela',max_length=80)
    nombre_direccion_trabajo_escuela = models.CharField('Nombre de la dirección del trabajo o escuela',max_length=35)
    fecha_ingreso_trabajo_escuela = models.DateField()
    ingreso_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_tentativa_viaje = models.DateField()
    correo = models.EmailField('Correo electrónico')
    tramite = models.ForeignKey('tramites.Tramite',verbose_name='Tramite',on_delete=models.CASCADE)

class DireccionEstadosUnidos(models.Model):
    calle = models.CharField('Calle', max_length=50)
    numero = models.PositiveIntegerField("Número")
    ciudad = models.CharField('Ciudad', max_length=40)
    estado = models.CharField('Estado',max_length=20)  
    codigo_postal = models.PositiveIntegerField('Código postal')
    nombre_direccion = models.CharField('Nombre del lugar',max_length=50,blank=True,null=True)

class RedSocial(models.Model):
    nombre = models.CharField('Red social',max_length=30)

# Aquí se almacenarán las redes sociales del solicitante de VISA.
class VisaRedSocial(models.Model):
    visa = models.ForeignKey('visas.Visa',on_delete=models.CASCADE)
    red_social = models.ForeignKey('visas.RedSocial',on_delete=models.CASCADE)
    url = models.URLField('Enlace del perfil')