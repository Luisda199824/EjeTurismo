# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 23:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelsAdmin', '0011_administrador_root'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marcador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=512)),
                ('latitud', models.CharField(max_length=128)),
                ('longitud', models.CharField(max_length=128)),
                ('interes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modelsAdmin.Interes')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelsAdmin.Usuario')),
            ],
            options={
                'verbose_name_plural': 'Marcadores',
                'verbose_name': 'Marcador',
            },
        ),
    ]
