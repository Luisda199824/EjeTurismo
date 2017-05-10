from django.contrib import admin

from .models import Noticia

@admin.register(Noticia)
class AdminNoticia(admin.ModelAdmin):
    list_display = ['titulo']
