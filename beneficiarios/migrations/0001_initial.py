# Generated by Django 3.2.3 on 2021-05-28 14:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiario',
            fields=[
                ('curp', models.CharField(max_length=18, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('/^([A-Z][AEIOUX][A-Z]{2}\\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\\d|3[01])[HM](?:AS|B[CS]|C[CLMSH]|D[FG]|G[TR]|HG|JC|M[CNS]|N[ETL]|OC|PL|Q[TR]|S[PLR]|T[CSL]|VZ|YN|ZS)[B-DF-HJ-NP-TV-Z]{3}[A-Z\\d])(\\d)$/')], verbose_name='CURP')),
                ('primer_apellido', models.CharField(max_length=50, verbose_name='Primer apellido')),
                ('segundo_apellido', models.CharField(max_length=50, verbose_name='Segundo apellido')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre(s)')),
                ('nombre_vialidad', models.CharField(max_length=50, verbose_name='Vialidad')),
                ('numero_exterior', models.IntegerField(verbose_name='Número exterior')),
                ('numero_interior', models.IntegerField(verbose_name='Número interior')),
                ('entre_vialidades', models.CharField(max_length=50, verbose_name='Entre vialidades')),
                ('descripcion_ubicacion', models.TextField(verbose_name='Referencias de ubicación')),
                ('estudio_socioeconomico', models.BooleanField(verbose_name='Presentó estudio socioeconómico')),
                ('jefe_familia', models.BooleanField(verbose_name='Es jefe de familia')),
                ('integrantes_familia', models.IntegerField(verbose_name='Número de integrantes de la familia')),
                ('dependientes_economicos', models.IntegerField(verbose_name='Número de dependeientes económicos')),
                ('numero_habitantes_vivienda', models.IntegerField(verbose_name='Número de habitantes en la vivienda')),
                ('vivienda_electricidad', models.BooleanField(default=False, verbose_name='Electricidad')),
                ('vivienda_agua', models.BooleanField(default=False, verbose_name='Agua corriente')),
                ('vivienda_drenaje', models.BooleanField(default=False, verbose_name='Drenaje')),
                ('vivienda_gas', models.BooleanField(default=False, verbose_name='Gas')),
                ('vivienda_telefono', models.BooleanField(default=False, verbose_name='Teléfono')),
                ('vivienda_internet', models.BooleanField(default=False, verbose_name='Internet')),
                ('beneficiario_colectivo', models.BooleanField(default=False, verbose_name='Es beneficiario colectivo')),
                ('asentamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.asentamiento', verbose_name='Asentamiento')),
                ('discapacidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.discapacidad', verbose_name='Discapacidad')),
                ('estado_civil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.estadocivil', verbose_name='Estado civíl')),
                ('grupo_vulnerable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.grupovulnerable', verbose_name='Grupo vulnerable')),
                ('identificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.identificacionoficial', verbose_name='Identificación Oficial')),
                ('ingreso_mensual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.ingresomensual', verbose_name='Ingreso mensual')),
                ('nivel_estudios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.nivelestudios', verbose_name='Nivel de estudios')),
                ('ocupacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.ocupacion', verbose_name='Ocupación')),
                ('tipo_seguridad_social', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.tiposeguridadsocial', verbose_name='Tipo de seguridad social')),
                ('tipo_vialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.tipovialidad', verbose_name='Tipo de vialidad')),
                ('vivienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.vivienda', verbose_name='Vivienda')),
            ],
        ),
    ]
