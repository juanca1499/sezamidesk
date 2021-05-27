from django.db import models
from django.core.validators import RegexValidator

class PersonaDesaparecida(models.Model):
    curp = models.CharField('CURP de la persona desaparecida',primary_key=True,max_length=18,validators=[RegexValidator(r'/^([A-Z][AEIOUX][A-Z]{2}\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])[HM](?:AS|B[CS]|C[CLMSH]|D[FG]|G[TR]|HG|JC|M[CNS]|N[ETL]|OC|PL|Q[TR]|S[PLR]|T[CSL]|VZ|YN|ZS)[B-DF-HJ-NP-TV-Z]{3}[A-Z\d])(\d)$/')])
    nombre_desaparecido = models.CharField('Nombre de la persona desaparecida',max_length=50)
    apellido_paterno_desaparecido = models.CharField('Apellido paterno de la persona desaparecida',max_length=50)
    apellido_materno_desaparecido = models.CharField('Apellido materno de la persona desaparecida',max_length=50,blank=True, null=True)
    fecha_nacimiento_desaparecido = models.DateField('Fecha de nacimiento de la persona desaparecida')
    observaciones = models.CharField('Observaciones',max_length=150)
    estatus = models.CharField('Estatus',max_length=30)
    ultimo_lugar = models.CharField('Último lugar donde fue visto',max_length=30)
    fecha_desaparicion = models.DateField('Fecha de desaparición')
    telefono_solicitante = models.CharField("Teléfono del solicitante",max_length=10,validators=[RegexValidator(r'^[0-9]\d*$')])
    nombre_solicitante = models.CharField('Nombre del solicitante',max_length=50)
    apellido_paterno_solicitante = models.CharField('Apellido paterno del solicitante',max_length=50)
    apellido_materno_solicitante = models.CharField('Apellido materno del solicitante',max_length=50,blank=True, null=True)

    def __str__(self):
        return self.nombre_desaparecido