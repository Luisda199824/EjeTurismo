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
    template = loader.get_template('recuperarPassword/index.html')
    ctx = {}
    return HttpResponse(template.render(ctx, request))

def generarHash():
    import string, random
    size = 40
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))
