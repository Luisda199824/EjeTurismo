from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from modelsAdmin.models import Suscriptor

def indexSuscriptor(request):
    if request.user is None and not request.user.is_authenticated():
        logout(request)
        print("Redir")
        return redirect('/')

    usuario = Suscriptor.objects.filter(usuario__usuario=request.user)[0]
    template = loader.get_template('suscriptor/index.html')
    ctx = {
        'nombre': usuario.usuario.nombre.title()
    }
    return HttpResponse(template.render(ctx, request))
