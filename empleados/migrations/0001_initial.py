# Generated by Django 3.2.3 on 2021-05-27 20:16

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('segundo_apellido', models.CharField(default='Segundo apellido', max_length=40, verbose_name='Apellido materno')),
                ('alias', models.CharField(default='alias', max_length=30, verbose_name='Alias')),
                ('telefono', models.CharField(max_length=15, null=True, verbose_name='Teléfono')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
