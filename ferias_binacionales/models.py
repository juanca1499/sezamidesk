from django.db import models
from django.core.validators import RegexValidator

class ConstanciaEstudios(models.Model):
    nombre = models.CharField(verbose_name="Nombre(s)",max_length=50)
    ap_paterno = models.CharField(verbose_name="Apellido Paterno", max_length=50)
    ap_materno = models.CharField(verbose_name="Apellido Materno", max_length=50)
    curp = models.CharField("CURP", primary_key = True, max_length=18, validators=[RegexValidator('([A-Z]{4}([0-9]{2})(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])[HM](AS|BC|BS|CC|CL|CM|CS|CH|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS|NE)[A-Z]{3}[0-9A-Z]\d)')])
    nivel_estudios = models.ForeignKey("catalogos.NivelEstudios", verbose_name="Nivel de estudios", on_delete=models.CASCADE)
    nombre_escuela = models.CharField(verbose_name="Nombre completo de la escuela", max_length=70)
    localidad = models.ForeignKey("catalogos.Localidad",verbose_name="Localidad", on_delete=models.CASCADE)
    anio_aprox = models.IntegerField(verbose_name="Año aproximado que se cursó el grado")
    fotografia = models.BooleanField(verbose_name="Fografía, reciente, de frente, sin lentes, sin gorra o sombrero",default=False)
    num_telefonico = models.CharField(verbose_name="Número de teléfono", validators=[RegexValidator('^\+?1?\d{9,15}$')], max_length=15)
    email = models.EmailField(verbose_name="Correo electrónico")

class DefensoriaPublica(models.Model):
    nombre = models.CharField(verbose_name="Nombre(s)",max_length=50)
    ap_paterno = models.CharField(verbose_name="Apellido Paterno", max_length=50)
    ap_materno = models.CharField(verbose_name="Apellido Materno", max_length=50)
    tramite_realizar = models.CharField(verbose_name="Trámite a Realizar", max_length=80)
    fecha = models.DateField(verbose_name="Fecha de trámite")
    localidad = models.ForeignKey("catalogos.Localidad",verbose_name="Localidad", on_delete=models.CASCADE)
    num_telefonico = models.CharField(verbose_name="Número de teléfono", validators=[RegexValidator('^\+?1?\d{9,15}$')], max_length=15)
    email = models.EmailField(verbose_name="Correo electrónico")

class LicenciaConducir(models.Model):
    nombre = models.CharField(verbose_name="Nombre(s)",max_length=50)
    ap_paterno = models.CharField(verbose_name="Apellido Paterno", max_length=50)
    ap_materno = models.CharField(verbose_name="Apellido Materno", max_length=50)
    acta_nacimiento = models.BooleanField(verbose_name="Acta de Nacimiento",default=False)
    comprobante_dom_eeuu = models.BooleanField(verbose_name="Comprobante de domicilio en Estados Unidos",default=False)
    referencia_dom_zac = models.BooleanField(verbose_name="Domicilio de referencia en el Estado de Zacatecas",default=False)
    fotografia = models.BooleanField(verbose_name="Fotografía",default=False)
    tipo_sangre = models.CharField(verbose_name="Tipo de Sangre", max_length=3)
    identificacion_oficial = models.BooleanField(verbose_name="Identificación oficial",default=False) 
    estatus = models.ForeignKey("tramites.EstadoTramite", verbose_name="Estatus de trámite", on_delete=models.CASCADE)

class ExpedicionActa(models.Model):
    nombre = models.CharField(verbose_name="Nombre(s)",max_length=50)
    ap_paterno = models.CharField(verbose_name="Apellido Paterno", max_length=50)
    ap_materno = models.CharField(verbose_name="Apellido Materno", max_length=50)
    nombre_solicitante = models.CharField(verbose_name="Nombre del solicitante", max_length=100)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    municipio_registro = models.CharField(verbose_name="Municipio de registro",max_length=30)

class DobleNacionalidad(models.Model):
    nombre = models.CharField(verbose_name="Nombre(s)",max_length=50)
    ap_paterno = models.CharField(verbose_name="Apellido Paterno", max_length=50)
    ap_materno = models.CharField(verbose_name="Apellido Materno", max_length=50)
    acta_nacimiento_original = models.BooleanField(verbose_name="Acta de Nacimiento Original",default=False)
    actas_apostilladas = models.BooleanField(verbose_name="Actas apostilladas",default=False)
    comprobante_domicilio = models.BooleanField(verbose_name="Identificación Oficial Padres",default=False)
    original_copias = models.BooleanField(verbose_name="Original y 2 Copias",default=False)    

class CorreccionActa(models.Model):
    nombre = models.CharField(verbose_name="Nombre(s)",max_length=50)
    ap_paterno = models.CharField(verbose_name="Apellido Paterno", max_length=50)
    ap_materno = models.CharField(verbose_name="Apellido Materno", max_length=50)
    acta_a_corregir = models.BooleanField(verbose_name="Acta a corregir",default=False)   
    documentos_comprobantes = models.BooleanField(verbose_name="Documentos que comprueben lo solicitado",default=False)
    testimonial = models.BooleanField(verbose_name="Testimonial de 2 personas",default=False)  
    solicitud_firmado = models.BooleanField(verbose_name="Solicitud firmada",default=False)    
    original_copias = models.BooleanField(verbose_name="Original y 2 Copias",default=False)   

class MandamientosJudiciales(models.Model):
    nombre = models.CharField(verbose_name="Nombre(s)",max_length=50)
    ap_paterno = models.CharField(verbose_name="Apellido Paterno", max_length=50)
    ap_materno = models.CharField(verbose_name="Apellido Materno", max_length=50)
    acta_nac_original = models.BooleanField(verbose_name="Acta de Nacimiento Original",default=False) 
    curp_act = models.BooleanField(verbose_name="CURP Actualizada",default=False) 
    comprobante_domicilio = models.BooleanField(verbose_name="Comprobante domicilio",default=False) 
    pasaporte_vigente = models.BooleanField(verbose_name="Pasaporte vigente",default=False) 
    matricula_consular = models.BooleanField(verbose_name="Matrícula Consular",default=False) 
    pago_en_caja_fiscalia = models.BooleanField(verbose_name="Pago que se realiza en caja de fiscalia",default=False) 
    fotografia= models.BooleanField(verbose_name="1 Fotografía tamaño infantil blanco y negro con fondo blanco",default=False) 
    ine_familiar = models.BooleanField(verbose_name="INE del familiar directo que va a tramitar el documento",default=False) 






