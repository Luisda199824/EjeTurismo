from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from modelsAdmin.models import Usuario, Root

def iniciarSesionRoot(request):
    error = (False, "")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            if len(User.objects.filter(username=username)) == 0:
                mensaje = "El usuario no fue encontrado"
            else:
                mensaje = "Contraseña incorrecta"
            error = (True, mensaje)
        else:
            root = Root.objects.filter(usuario__usuario=user)

            if len(root) == 0:
                error = (True, "No hay cuenta asociada")
            else:
                login(request, user)
                return redirect('/root')

    template = loader.get_template('iniciarSesionRoot/index.html')
    ctx = {
        'error': error
    }
    return HttpResponse(template.render(ctx, request))
