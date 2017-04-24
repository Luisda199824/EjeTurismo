from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from modelsAdmin.models import Usuario, Administrador, Suscriptor

def indexAdmin(request):
    template = loader.get_template('administrador/index.html')
    ctx = {}
    return HttpResponse(template.render(ctx, request))
