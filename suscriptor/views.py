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

    noticias = Noticia.objects.all()[::-1]
    intereses = []
    municipios = []

    for noticia in noticias:
        noticia.is_video = str(noticia.imagen).endswith(".mp4") or str(noticia.imagen).endswith(".avi")
        noticia.imagen = str(noticia.imagen)
        interes = noticia.interes
        if not interes in intereses:
            intereses.append(interes)

        municipio = noticia.administrador.municipio
        if not municipio in municipios:
            municipios.append(municipio)

    template = loader.get_template('suscriptor/index.html')
    ctx = {
        'nombre': usuario.usuario.nombre.title(),
        'noticias': noticias,
        'intereses': intereses,
        'municipios': municipios,
    }
    return HttpResponse(template.render(ctx, request))

def deactivateSuscriptor(request):
    if not request.user.is_authenticated():
        logout(request)
        return redirect('/')

    usuario = Suscriptor.objects.filter(usuario__usuario=request.user)[0]

    if request.method=="POST" and "eliminar" in request.POST:
        usuario.estadoCuenta = False
        usuario.save()
        return redirect('/cuentaEliminada')

    template = loader.get_template('suscriptor/desactivar_cuenta.html')
    ctx = {
        'nombre': usuario.usuario.nombre.title(),
    }
    return HttpResponse(template.render(ctx, request))
