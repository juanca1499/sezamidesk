# Generated by Django 3.2.3 on 2021-06-01 06:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empleados', '0002_auto_20210528_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visa',
            fields=[
                ('curp', models.CharField(max_length=18, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('([A-Z]{4}([0-9]{2})(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])[HM](AS|BC|BS|CC|CL|CM|CS|CH|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS|NE)[A-Z]{3}[0-9A-Z]\\d)')], verbose_name='CURP')),
                ('pasaporte', models.BooleanField(default=False, verbose_name='Pasaporte')),
                ('direccion_usa', models.CharField(max_length=70, verbose_name='Dirección de Estados Unidos')),
                ('persona_visitar', models.CharField(max_length=70, verbose_name='Nombre de la persona a visitar')),
                ('tel_persona_visitar', models.CharField(max_length=10, verbose_name='Teléfono de la persona a visitar')),
                ('fe_nacimiento_madre', models.DateField(verbose_name='Fecha de nacimiento de la madre')),
                ('fe_nacimiento_padre', models.DateField(verbose_name='Fecha de nacimiento del padre')),
                ('dir_trabajo_escuela', models.CharField(max_length=80, verbose_name='Dirección del lugar de trabajo o escuela')),
                ('nom_dir_trabajo_escuela', models.CharField(max_length=35, verbose_name='Nombre de la dirección del trabajo o escuela')),
                ('fe_ingreso_trabajo_escuela', models.DateField(verbose_name='Fecha de ingreso al trabajo o escuela')),
                ('ingreso_mensual', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ingreso Mensual')),
                ('fecha_viaje', models.DateField(verbose_name='Fecha tentativa de viaje')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('red_social', models.URLField(verbose_name='URL de la red social')),
                ('pago', models.BooleanField(default=False)),
                ('asesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.empleado')),
            ],
        ),
    ]