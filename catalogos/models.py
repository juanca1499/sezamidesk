from django.db import models

class IdentificacionOficial(models.Model):
    identificacion = models.CharField('Tipo de identificación', max_length=30)

class TipoVialidad(models.Model):
    vialidad = models.CharField('Tipo de vialidad', max_length=20)

class EstadoCivil(models.Model):
    estado_civil = models.CharField('Estado Civil',max_length=20)

class Ocupacion(models.Model):
    ocupacion = models.CharField('Tipo de ocupación', max_length=30)

# class IngresoMensual


class Vivienda(models.Model):
    vivienda = models.CharField('Tipo de vivienda', max_length=20)

class NivelEstudios(models.Model):
    nivel_estudio = models.CharField('Nivel de estudios', max_length=20)

class TipoSeguridadSocial(models.Model):
    seguridad_social = models.CharField('Seguridad social', max_length=20)

class Discapacidad(models.Model):
    discapacidad = models.CharField('Tipo de discapacidad', max_length=60)

class GrupoVulnerable(models.Model):
    grupo_vulnerable = models.CharField('Grupo vulnerable', max_length=80)