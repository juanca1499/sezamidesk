# Generated by Django 3.2.3 on 2021-06-01 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0002_auto_20210528_1805'),
        ('visas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visa',
            name='asesor',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empleados.empleado'),
        ),
    ]