# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0004_noticia_interes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='imagen',
        ),
        migrations.AddField(
            model_name='noticia',
            name='archivo',
            field=models.FileField(default=0, upload_to='noticias/'),
            preserve_default=False,
        ),
    ]
