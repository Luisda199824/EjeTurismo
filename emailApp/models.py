from django.db import models
from django.contrib.auth.models import User

class PasswordRestaure(models.Model):
    user = models.ForeignKey(User)
    hash = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Restaurar contraseña'
        verbose_name_plural = 'Restaurar contraseñas'

    def __unicode__(self):
        return "Recuperador de contraseña"
