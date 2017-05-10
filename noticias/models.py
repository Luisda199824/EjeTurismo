from django.db import models

from modelsAdmin.models import Administrador

class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=25550)
    imagen = models.ImageField(upload_to="noticias")
    administrador = models.ForeignKey(Administrador)

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    def __str__(self):
        return self.titulo

    def __unicode__(self):
        return self.titulo
