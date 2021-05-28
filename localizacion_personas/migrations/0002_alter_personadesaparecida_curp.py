# Generated by Django 3.2.3 on 2021-05-28 17:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localizacion_personas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personadesaparecida',
            name='curp',
            field=models.CharField(max_length=18, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('([A-Z]{4}([0-9]{2})(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])[HM](AS|BC|BS|CC|CL|CM|CS|CH|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS|NE)[A-Z]{3}[0-9A-Z]\\d)')], verbose_name='CURP de la persona desaparecida'),
        ),
    ]
