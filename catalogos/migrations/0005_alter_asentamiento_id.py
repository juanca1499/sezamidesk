# Generated by Django 3.2.3 on 2021-05-27 16:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0004_alter_asentamiento_tipo_asentamiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asentamiento',
            name='id',
            field=models.CharField(max_length=13, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[1-9]\\d*$')], verbose_name='ID'),
        ),
    ]
