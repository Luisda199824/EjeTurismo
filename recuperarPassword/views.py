from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from emailApp.models import PasswordRestaure

from .tasks import enviarCorreoRecuperarPassword

from modelsAdmin.models import Usuario
from django.contrib.auth.models import User

def resetPassword(request):
    error = (False, "")
    exito = (False, "")
    if request.method == "POST":
        user = request.POST.get("user")

        if user is None:
            error = (True, "Ingrese un usuario")
        elif len(user) == 0:
            error = (True, "Ingrese un usuario")
        else:
            users = User.objects.filter(username=user)
            if len(users) == 0:
                error = (True, "El usuario no fue encontrado")
            else:
                hash = generarHash()
                pr = PasswordRestaure(user=users[0], hash=hash)
                pr.save()
                enviarCorreoRecuperarPassword(pr.id)

                exito = (True, "Correo enviado correctamente")

    template = loader.get_template('recuperarPassword/index.html')
    ctx = {
        "error": error,
        "exito": exito,
    }
    return HttpResponse(template.render(ctx, request))

def changePasswordWithHash(request, hash):
    error = (False, "")
    exito = (False, "")
    usuario = None
    pr = PasswordRestaure.objects.filter(hash=hash)
    if len(pr) != 0:
        pr = pr[0]
        usuario = pr.user
    else:
        error = (True, "Petición no encontrada")

    if request.method == "POST" and not error[0]:
        form = request.POST
        new_password = form.get("new_password")
        new_password_2 = form.get("new_password_2")

        if new_password is not None and new_password_2 is not None:
            if new_password == new_password_2:
                usuario.set_password(new_password)
                usuario.save()
                pr.delete()
                exito = (True, "Contraseña cambiada correctamente")
        else:
            error = (True, "Problemas al cambiar la contraseña")

    template = loader.get_template('recuperarPassword/change.html')
    ctx = {
        'error': error,
        'usuario': usuario,
        'exito': exito,
    }
    return HttpResponse(template.render(ctx, request))

def generarHash():
    import string, random
    size = 40
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))
