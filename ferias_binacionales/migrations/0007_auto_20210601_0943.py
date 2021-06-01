# Generated by Django 3.2.3 on 2021-06-01 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ferias_binacionales', '0006_auto_20210601_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constanciaestudios',
            name='anio_aprox',
            field=models.IntegerField(verbose_name='Año aproximado que se cursó el grado'),
        ),
        migrations.AlterField(
            model_name='constanciaestudios',
            name='ap_materno',
            field=models.CharField(max_length=50, verbose_name='Apellido Materno'),
        ),
        migrations.AlterField(
            model_name='constanciaestudios',
            name='fotografia',
            field=models.BooleanField(default=False, verbose_name='Fografía, reciente, de frente, sin lentes, sin gorra o sombrero'),
        ),
        migrations.AlterField(
            model_name='constanciaestudios',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre(s)'),
        ),
    ]
