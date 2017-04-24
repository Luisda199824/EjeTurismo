from django.contrib import admin

from .models import *

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['dni','nombre','apellido','direccion','telefono','ciudad','email','fecha_nacimiento','genero','pais','usuario']

@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ['usuario','estadoCuenta','municipio']

@admin.register(Suscriptor)
class SuscriptorAdmin(admin.ModelAdmin):
    list_display = ['administrador','estadoCuenta','usuario']
