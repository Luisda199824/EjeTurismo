from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from modelsAdmin.models import Suscriptor
from noticias.models import Noticia

def indexSuscriptor(request):
    if not request.user.is_authenticated():
        logout(request)
        return redirect('/')

    usuario = Suscriptor.objects.filter(usuario__usuario=request.user)[0]

    noticias = Noticia.objects.filter(administrador=usuario.administrador)

    template = loader.get_template('suscriptor/index.html')
    ctx = {
        'nombre': usuario.usuario.nombre.title(),
        'noticias': noticias,
    }
    return HttpResponse(template.render(ctx, request))
