from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth import login, authenticate, logout

from modelsAdmin.models import Usuario, Root

def registerUsuario(request):
    template = loader.get_template('registroUsuarios/index.html')
    ctx = {}
    return HttpResponse(template.render(ctx, request))
