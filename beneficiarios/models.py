from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Beneficiario(models.Model):
    
    curp = models.CharField("CURP", primary_key = True, max_length=18, validators=[RegexValidator(r'/^([A-Z][AEIOUX][A-Z]{2}\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])[HM](?:AS|B[CS]|C[CLMSH]|D[FG]|G[TR]|HG|JC|M[CNS]|N[ETL]|OC|PL|Q[TR]|S[PLR]|T[CSL]|VZ|YN|ZS)[B-DF-HJ-NP-TV-Z]{3}[A-Z\d])(\d)$/')])
    primer_apellido = models.CharField("Primer apellido", max_length=50)
    segundo_apellido = models.CharField("Segundo apellido", max_length=50)
    nombre = models.CharField("Nombre(s)", max_length=50)
    identificacion = models.ForeignKey("catalogos.IdentificacionOficial", verbose_name="Identificación Oficial", on_delete=models.CASCADE)
    tipo_vialidad = models.ForeignKey("catalogos.TipoVialidad", verbose_name="Tipo de vialidad", on_delete=models.CASCADE)
    nombre_vialidad = models.CharField("Vialidad", max_length=50)
    numero_exterior = models.IntegerField("Número exterior")
    numero_interior = models.IntegerField("Número interior")
    asentamiento = models.ForeignKey("catalogos.Asentamiento", verbose_name="Asentamiento", on_delete=models.CASCADE)
    entre_vialidades = models.CharField("Entre vialidades", max_length=50)
    descripcion_ubicacion = models.TextField("Referencias de ubicación")
    estudio_socioeconomico = models.BooleanField("Presentó estudio socioeconómico")
    estado_civil = models.ForeignKey("catalogos.EstadoCivil", verbose_name="Estado civíl", on_delete=models.CASCADE)
    jefe_familia = models.BooleanField("Es jefe de familia")
    ocupacion = models.ForeignKey("catalogos.Ocupacion", verbose_name="Ocupación", on_delete=models.CASCADE)
    ingreso_mensual = models.ForeignKey("catalogos.IngresoMensual", verbose_name="Ingreso mensual", on_delete=models.CASCADE)
    integrantes_familia = models.IntegerField("Número de integrantes de la familia")
    dependientes_economicos = models.IntegerField("Número de dependeientes económicos")
    vivienda = models.ForeignKey("catalogos.Vivienda", verbose_name="Vivienda", on_delete=models.CASCADE)
    numero_habitantes_vivienda = models.IntegerField("Número de habitantes en la vivienda")
    vivienda_electricidad = models.BooleanField("Electricidad", default = False)
    vivienda_agua = models.BooleanField("Agua corriente", default = False)
    vivienda_drenaje = models.BooleanField("Drenaje", default = False)
    vivienda_gas = models.BooleanField("Gas", default = False)
    vivienda_telefono = models.BooleanField("Teléfono", default = False)
    vivienda_internet = models.BooleanField("Internet", default = False)
    nivel_estudios = models.ForeignKey("catalogos.NivelEstudios", verbose_name="Nivel de estudios", on_delete=models.CASCADE)
    tipo_seguridad_social = models.ForeignKey("catalogos.TipoSeguridadSocial", verbose_name="Tipo de seguridad social", on_delete=models.CASCADE)
    discapacidad = models.ForeignKey("catalogos.Discapacidad", verbose_name="Discapacidad", on_delete=models.CASCADE)
    grupo_vulnerable = models.ForeignKey("catalogos.GrupoVulnerable", verbose_name="Grupo vulnerable", on_delete=models.CASCADE)
    beneficiario_colectivo = models.BooleanField("Es beneficiario colectivo", default = False)
    
    

    # foreign keys
       





