from django.db import models

from django.contrib.auth.models import User
from datetime import datetime

class Usuario(models.Model):
    # TODO: Define fields here
    dni = models.CharField(max_length=8)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.IntegerField()
    ciudad = models.CharField(blank=True, max_length=255)
    email = models.CharField(blank=True, max_length=255)
    fecha_nacimiento = models.DateField(default=datetime.today)
    genero = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    usuario = models.ForeignKey(User)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __unicode__(self):
        pass
