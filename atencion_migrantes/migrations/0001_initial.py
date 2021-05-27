# Generated by Django 3.2.3 on 2021-05-27 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AtencionMigrantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion_oficial', models.BooleanField(verbose_name='Identificación Oficial')),
                ('curp', models.BooleanField(verbose_name='CURP')),
                ('rfc', models.BooleanField(verbose_name='RFC')),
                ('solicitud_gobernador', models.BooleanField(verbose_name='Solicitud al gobernador')),
                ('hoja_deportacion', models.BooleanField(verbose_name='Hoja de deportación')),
                ('comprobante_domicilio', models.BooleanField(verbose_name='Comprobante de domicilio')),
                ('acta_nacimiento', models.BooleanField(verbose_name='Comprobante de domicilio')),
            ],
        ),
    ]
