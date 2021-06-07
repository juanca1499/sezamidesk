from django.db import models
from django.core.validators import RegexValidator



class Tramite(models.Model):
    beneficiario = models.ForeignKey("beneficiarios.Beneficiario",verbose_name='Beneficiario',on_delete=models.CASCADE, null = True)
    empleado = models.ForeignKey("empleados.Empleado",verbose_name='Empleado',on_delete=models.CASCADE)
    grupo = models.ForeignKey("tramites.Grupo",verbose_name="Grupo",on_delete=models.CASCADE,null=True,default=None)
    estado = models.ForeignKey("tramites.EstadoTramite",verbose_name='Estado',on_delete=models.CASCADE)
    fecha_inicio = models.DateField('Fecha de Inicio',auto_now_add=True)
    fecha_fin = models.DateField('Fecha de fin',null = True)

class EstadoTramite(models.Model):
    estado = models.CharField("Estado de tramite",max_length=10)

    def __str__(self):
        return self.estado

class Grupo(models.Model):
    nombre = models.CharField("Nombre del grupo",max_length=50)
    representante = models.ForeignKey("tramites.Representante", verbose_name="Representante", on_delete=models.CASCADE)
    club = models.ForeignKey("tramites.Club", verbose_name="Club", on_delete=models.CASCADE)

class Representante(models.Model):
    primer_apellido = models.CharField("Primer apellido", max_length=50)
    segundo_apellido = models.CharField("Segundo apellido", max_length=50)
    nombre = models.CharField("Nombre(s)", max_length=50)

class Club(models.Model):
    nombre = models.CharField("Nombre del club",max_length=50)
    nombre_presidente = models.CharField("Nombre del presidente(a)",max_length=60)
    correo_presidente = models.EmailField(max_length=254)
    direccion = models.CharField("Dirección del club",max_length=80)
    num_telefonico = models.CharField(verbose_name="Número de teléfono", validators=[RegexValidator('^+?1?\d{9,15}$')], max_length=15)