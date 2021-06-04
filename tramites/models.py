from django.db import models


class Tramite(models.Model):
    beneficiario = models.ForeignKey("beneficiarios.Beneficiario",verbose_name='Beneficiario',on_delete=models.CASCADE, null = True)
    empleado = models.ForeignKey("empleados.Empleado",verbose_name='Empleado',on_delete=models.CASCADE)
    estado = models.ForeignKey("tramites.EstadoTramite",verbose_name='Estado',on_delete=models.CASCADE)
    fecha_inicio = models.DateField('Fecha de Inicio',auto_now_add=True)
    fecha_fin = models.DateField('Fecha de fin',null = True)

class EstadoTramite(models.Model):
    estado = models.CharField("Estado de tramite",max_length=10)

    def __str__(self):
        return self.estado