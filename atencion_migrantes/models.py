from django.db import models

# Create your models here.
class AtencionMigrantes(models.Model):
    identificacion_oficial = models.BooleanField("Identificación Oficial")
    curp = models.BooleanField("CURP")
    rfc = models.BooleanField("RFC")
    solicitud_gobernador = models.BooleanField("Solicitud al gobernador")
    hoja_deportacion = models.BooleanField("Hoja de deportación")
    comprobante_domicilio = models.BooleanField("Comprobante de domicilio")
    acta_nacimiento = models.BooleanField("Comprobante de domicilio")
    
    # Foreign keys
    tramite = models.ForeignKey("tramites.Tramite", verbose_name="Trámite", on_delete=models.CASCADE)

