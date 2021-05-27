# Generated by Django 3.2.3 on 2021-05-27 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apostilla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acta_americana', models.BooleanField(default=False, verbose_name='Acta americana')),
                ('acta_mexicana', models.BooleanField(default=False, verbose_name='Acta mexicana')),
                ('identificacion_padres', models.BooleanField(default=False, verbose_name='Identificación oficial de ambos padres')),
                ('curp', models.BooleanField(default=False, verbose_name='CURP')),
                ('comprobante_domicilio', models.BooleanField(default=False, verbose_name='Comprobante de domicilio')),
                ('rfc', models.BooleanField(default=False, verbose_name='RFC')),
            ],
        ),
    ]