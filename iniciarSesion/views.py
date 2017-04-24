from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth import login, authenticate, logout

from modelsAdmin.models import Usuario, Administrador, Suscriptor

def iniciarSesion(request):
    error = (False, "")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is None:
            error = (True, "El usuario no fue encontrado")
        else:
            suscriptores = Suscriptor.objects.filter(usuario__usuario=user)
            administradores = Administrador.objects.filter(usuario__usuario=user)

            if "btn_usuario" in request.POST:
                if len(suscriptores) == 0:
                    error = (True, "No hay cuenta asociada")
                else:
                    if suscriptores[0].estadoCuenta:
                        login(request, user)
                        return redirect('/user')
                    else:
                        error = (True, "Su cuenta no ha sido activada")

            if "btn_administrador" in request.POST:
                if len(administradores) == 0:
                    error = (True, "No hay cuenta asociada")
                else:
                    if administradores[0].estadoCuenta:
                        login(request, user)
                        return redirect('/administrator')
                    else:
                        error = (True, "Su cuenta no ha sido activada")

    template = loader.get_template('iniciarSesion/index.html')
    ctx = {
        'error': error
    }
    return HttpResponse(template.render(ctx, request))
