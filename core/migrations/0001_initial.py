# Generated by Django 3.1.7 on 2021-06-29 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('idCategoria', models.CharField(default='', max_length=20, primary_key=True, serialize=False, verbose_name='idCategoria')),
                ('nombreServicio', models.CharField(default='', max_length=50, verbose_name='nombreServicio')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('rut', models.CharField(default='', max_length=50, primary_key=True, serialize=False, verbose_name='rut')),
                ('nombreProveedor', models.CharField(default='', max_length=50, verbose_name='nombreProveedor')),
                ('descripcion', models.CharField(default='', max_length=500, verbose_name='descripcion')),
                ('telefono', models.CharField(default='', max_length=50, verbose_name='telefono')),
                ('emailProveedor', models.CharField(default='', max_length=50, verbose_name='emailProveedor')),
                ('tipoServicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.servicio')),
            ],
        ),
    ]
