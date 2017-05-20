
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class Usuario(models.Model):
    dni = models.CharField(max_length=20)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=100)
    ciudad = models.CharField(blank=True, max_length=255)
    email = models.CharField(blank=True, max_length=255)
    fecha_nacimiento = models.DateField(default=datetime.today)
    genero = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    usuario = models.ForeignKey(User)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.nombre + " " + self.apellido

    def __unicode__(self):
        return self.nombre + " " + self.apellido

class Root(models.Model):
    usuario = models.ForeignKey(Usuario)

    class Meta:
        verbose_name = 'Usuario Root'
        verbose_name_plural = 'Usuarios Root'

    def __unicode__(self):
        return str(self.usuario)
        return self.nombre + " " + self.apellido

class Administrador(models.Model):
    root = models.ForeignKey(Root)
    usuario = models.ForeignKey(Usuario)
    estadoCuenta = models.BooleanField(default=True)
    municipio = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'

    def __unicode__(self):
        return str(self.usuario)

class Suscriptor(models.Model):
    administrador = models.ForeignKey(Administrador)
    usuario = models.ForeignKey(Usuario)
    estadoCuenta = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores'

    def __unicode__(self):
        return str(self.usuario)

class ListaSolicitudesAdministrador(models.Model):
    administrador = models.ForeignKey(Administrador)
    evaluada = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Lista de solicitudes del Administrador'
        verbose_name_plural = 'Lista de solicitudes del Administrador'

    def __unicode__(self):
        return "Evaluación: " + str(self.administrador.usuario)
        return str(self.usuario)

class ListaSolicitudesSuscriptor(models.Model):
    suscriptor = models.ForeignKey(Suscriptor)
    evaluada = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Lista de solicitudes del Suscriptor'
        verbose_name_plural = 'Lista de solicitudes del Suscriptores'

    def __unicode__(self):
        return "Evaluación: " + str(self.suscriptor.usuario)

class Interes(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Interes'
        verbose_name_plural = 'Intereses'

    def __unicode__(self):
        return self.nombre

class ListaInteresAdministrador(models.Model):
    administrador = models.ForeignKey(Administrador)
    interes = models.ForeignKey(Interes)

    class Meta:
        verbose_name = 'Lista de intereses de Administradores'
        verbose_name_plural = 'Lista de intereses de Administradores'

    def __unicode__(self):
        return "Interes: %s Administrador: %s" % (self.interes.nombre, str(self.administrador.usuario))
        return self.nombre

class ListaInteresSuscriptor(models.Model):
    suscriptor = models.ForeignKey(Suscriptor)
    interes = models.ForeignKey(Interes)

    class Meta:
        verbose_name = 'Lista de intereses de Suscriptores'
        verbose_name_plural = 'Lista de intereses de Suscriptores'

    def __unicode__(self):
        return "Interes: %s Suscriptor: %s" % (self.interes.nombre, str(self.suscriptor.usuario))

class Marcador(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=512)
    usuario = models.ForeignKey(Usuario)
    interes = models.ForeignKey(Interes, null=True)
    latitud = models.CharField(max_length=128)
    longitud = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Marcador'
        verbose_name_plural = 'Marcadores'

    def __str__(self):
        return ""

