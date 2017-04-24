from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from modelsAdmin.models import Usuario, Root, Suscriptor, ListaSolicitudesAdministrador

def indexRoot(request):
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
        nombre = form.get("nombre")
        apellido = form.get("apellido")
        dni = form.get("dni")
        direccion = form.get("direccion")
        telefono = form.get("telefono")
        email = form.get("email")
        ciudad = form.get("ciudad")
        genero = form.get("genero")
        pais = form.get("pais")

        len_nombre = len(nombre)
        len_apellido = len(apellido)
        len_dni = len(dni)
        len_direccion = len(direccion)
        len_telefono = len(telefono)
        len_email = len(email)
        len_ciudad = len(ciudad)
        len_genero = len(genero)
        len_pais = len(pais)

        if (len_nombre*len_apellido*len_dni*len_direccion*len_telefono*len_email*len_ciudad*len_genero*len_pais) == 0:
            error = (True, "Debe ingresar todos los campos")
        else:
            administrador = Root.objects.filter(usuario__usuario=request.user)[0]

            from datetime import datetime

            usuario = administrador.usuario
            usuario.dni=dni
            usuario.nombre=nombre
            usuario.apellido=apellido
            usuario.direccion=direccion
            usuario.telefono=telefono
            usuario.ciudad=ciudad
            usuario.email=email
            usuario.genero=genero
            usuario.pais=pais
            usuario.fecha_nacimiento=datetime.now()
            usuario.save()

            return redirect('/root?e=mi')

    administrador = Root.objects.filter(usuario__usuario=request.user)[0]
    nombre = administrador.usuario.nombre
    apellido =  administrador.usuario.apellido
    dni =  administrador.usuario.dni
    direccion =  administrador.usuario.direccion
    telefono =  administrador.usuario.telefono
    email =  administrador.usuario.email
    ciudad =  administrador.usuario.ciudad
    genero =  administrador.usuario.genero
    pais =  administrador.usuario.pais
    password =  administrador.usuario.usuario.password
    template = loader.get_template('root/modificar_perfil.html')
    ctx = {
        'error': error,
        'exito': exito,
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "direccion": direccion,
        "telefono": telefono,
        "email": email,
        "ciudad": ciudad,
        "genero": genero,
        "pais": pais,
        "password": password,
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
