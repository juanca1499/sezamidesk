# Generated by Django 3.2.3 on 2021-06-04 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empleados', '0001_initial'),
        ('beneficiarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoTramite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=10, verbose_name='Estado de tramite')),
            ],
        ),
        migrations.CreateModel(
            name='Tramite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField(auto_now_add=True, verbose_name='Fecha de Inicio')),
                ('fecha_fin', models.DateField(null=True, verbose_name='Fecha de fin')),
                ('beneficiario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='beneficiarios.beneficiario', verbose_name='Beneficiario')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.empleado', verbose_name='Empleado')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tramites.estadotramite', verbose_name='Estado')),
            ],
        ),
    ]
