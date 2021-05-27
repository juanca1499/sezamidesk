from django.db import models

class Apostilla(models.Model):
    acta_americana = models.BooleanField('Acta americana',default=False)
    acta_mexicana = models.BooleanField('Acta mexicana',default=False)
    identificacion_padres = models.BooleanField('Identificación oficial de ambos padres',default=False)
    curp = models.BooleanField('CURP',default=False)
    comprobante_domicilio = models.BooleanField('Comprobante de domicilio',default=False)
    rfc = models.BooleanField('RFC',default=False)
    #tramite = models.ForeignKey('tramites.Tramite',verbose_name='Tramite',on_delete=models.CASCADE)