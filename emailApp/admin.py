from django.contrib import admin

from .models import PasswordRestaure

@admin.register(PasswordRestaure)
class AdminPasswordRestaure(admin.ModelAdmin):
    list_display = ['user', 'hash']
