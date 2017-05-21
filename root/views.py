from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from modelsAdmin.models import Usuario, Root, Suscriptor, ListaSolicitudesAdministrador

def indexRoot(request):
    if request.user is None:
        return redirect('/logout')
    
    if len(Root.objects.filter(usuario__usuario=request.user)) == 0:
        return redirect('/logout')    
        
    try:
        exito = request.GET.get("e")
        if exito == "mi":
            exito = (True, "Infomación modificada")
        else:
            exito = (False, "")
    except Exception as e:
        exito = (False, "")

    template = loader.get_template('root/index.html')
    ctx = {
        "exito": exito
    }
    return HttpResponse(template.render(ctx, request))

def modificarPerfilRoot(request):
    if not request.user.is_authenticated():
        logout(request)
        return redirect('/')

    error = (False, "")
    exito = (False, "")
    if request.method == "POST":
        form = request.POST
        old_password = form.get("old_password")
        new_password = form.get("new_password")
        new_password_2 = form.get("new_password_2")

        len_old_password = len(old_password)
        len_new_password = len(new_password)
        len_new_password_2 = len(new_password_2)

        if (len_old_password*len_new_password*len_new_password_2) == 0:
            error = (True, "Debe ingresar todos los campos")
        else:
            administrador = Root.objects.filter(usuario__usuario=request.user)[0]
            user = authenticate(username=request.user.username, password=old_password)
            if user is not None:
                if new_password == new_password_2:
                    request.user.set_password(new_password)
                    request.user.save()
                    return redirect('/root?e=mi')
                else:
                    error = (True, "La contraseñas no coinciden")
            else:
                error = (True, "La contraseña no es correcta")

    template = loader.get_template('root/modificar_perfil.html')
    ctx = {
        'error': error,
        'exito': exito,
    }
    return HttpResponse(template.render(ctx, request))

def solicitudesRoot(request):
    if not request.user.is_authenticated():
        logout(request)
        return redirect('/')

    root = Root.objects.filter(usuario__usuario=request.user)
    template = loader.get_template('root/solicitudes.html')
    solicitudes = ListaSolicitudesAdministrador.objects.filter(administrador__root=root)
    ctx = {
        'solicitudes': solicitudes
    }
    return HttpResponse(template.render(ctx, request))

def applySolicitudRoot(request, id_solicitud):
    if not request.user.is_authenticated():
        logout(request)
        return redirect('/')

    administrador = Root.objects.filter(usuario__usuario=request.user)[0]
    solicitud = ListaSolicitudesAdministrador.objects.filter(id=id_solicitud)
    if len(solicitud) == 0:
        mensaje = "No se encontró la solicitud"
    else:
        solicitud = solicitud[0]
        solicitud.evaluada = True
        solicitud.administrador.estadoCuenta = True
        solicitud.administrador.save()
        solicitud.save()
        mensaje = "Habilitado correctamente"
    template = loader.get_template('root/apply.html')
    ctx = {
        'mensaje': mensaje,
    }
    return HttpResponse(template.render(ctx, request))

def removeSolicitudRoot(request, id_solicitud):
    if not request.user.is_authenticated():
        logout(request)
        return redirect('/')

    administrador = Root.objects.filter(usuario__usuario=request.user)[0]
    solicitud = ListaSolicitudesAdministrador.objects.filter(id=id_solicitud)
    if len(solicitud) == 0:
        mensaje = "No se encontró la solicitud"
    else:
        solicitud = solicitud[0]
        solicitud.evaluada = False
        solicitud.administrador.estadoCuenta = False
        solicitud.administrador.save()
        solicitud.save()
        mensaje = "Deshabilitado correctamente"
    template = loader.get_template('root/apply.html')
    ctx = {
        'mensaje': mensaje,
    }
    return HttpResponse(template.render(ctx, request))
