from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from modelsAdmin.models import Usuario, Administrador, Suscriptor, ListaSolicitudesSuscriptor
from noticias.models import Noticia

def indexAdmin(request):
    try:
        exito = request.GET.get("e")
        if exito == "mi":
            exito = (True, "Infomación modificada")
        else:
            exito = (False, "")
    except Exception as e:
        exito = (False, "")

    template = loader.get_template('administrador/index.html')
    ctx = {
        "exito": exito
    }
    return HttpResponse(template.render(ctx, request))

def modificarPerfilAdmin(request):
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
        municipio = form.get("municipio")

        len_nombre = len(nombre)
        len_apellido = len(apellido)
        len_dni = len(dni)
        len_direccion = len(direccion)
        len_telefono = len(telefono)
        len_email = len(email)
        len_ciudad = len(ciudad)
        len_genero = len(genero)
        len_pais = len(pais)
        len_municipio = len(municipio)

        if (len_nombre*len_apellido*len_dni*len_direccion*len_telefono*len_email*len_ciudad*len_genero*len_pais) == 0:
            error = (True, "Debe ingresar todos los campos")
        else:
            if "btn_administrador" in form and (len(municipio) == 0):
                error = (True, "Seleccione un municipio")
            else:
                administrador = Administrador.objects.filter(usuario__usuario=request.user)[0]

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
                administrador.municipio = municipio
                administrador.save()

                return redirect('/administrador?e=mi')

    administrador = Administrador.objects.filter(usuario__usuario=request.user)[0]
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
    municipio =  administrador.municipio
    template = loader.get_template('administrador/modificar_perfil.html')
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
        "municipio": municipio,
    }
    return HttpResponse(template.render(ctx, request))

def solicitudesAdmin(request):
    if not request.user.is_authenticated():
        logout(request)
        return redirect('/')

    administrador = Administrador.objects.filter(usuario__usuario=request.user)[0]
    template = loader.get_template('administrador/solicitudes.html')
    solicitudes = ListaSolicitudesSuscriptor.objects.filter(suscriptor__administrador=administrador)
    print(solicitudes)
    ctx = {
        'solicitudes': solicitudes
    }
    return HttpResponse(template.render(ctx, request))
    return HttpResponse(template.render(ctx, request))

def applySolicitudAdmin(request, id_solicitud):
    if not request.user.is_authenticated():
        logout(request)
        return redirect('/')

    administrador = Administrador.objects.filter(usuario__usuario=request.user)[0]
    solicitud = ListaSolicitudesSuscriptor.objects.filter(id=id_solicitud)
    if len(solicitud) == 0:
        mensaje = "No se encontró la solicitud"
    else:
        solicitud = solicitud[0]
        solicitud.evaluada = True
        solicitud.suscriptor.estadoCuenta = True
        solicitud.suscriptor.save()
        solicitud.save()
        mensaje = "Habilitado correctamente"
    template = loader.get_template('administrador/apply.html')
    ctx = {
        'mensaje': mensaje,
    }
    return HttpResponse(template.render(ctx, request))
    return HttpResponse(template.render(ctx, request))

def removeSolicitudAdmin(request, id_solicitud):
    if not request.user.is_authenticated():
        logout(request)
        return redirect('/')

    administrador = Administrador.objects.filter(usuario__usuario=request.user)[0]
    solicitud = ListaSolicitudesSuscriptor.objects.filter(id=id_solicitud)
    if len(solicitud) == 0:
        mensaje = "No se encontró la solicitud"
    else:
        solicitud = solicitud[0]
        solicitud.evaluada = False
        solicitud.suscriptor.estadoCuenta = False
        solicitud.suscriptor.save()
        solicitud.save()
        mensaje = "Deshabilitado correctamente"
    template = loader.get_template('administrador/apply.html')
    ctx = {
        'mensaje': mensaje,
    }
    return HttpResponse(template.render(ctx, request))

def newNotice(request):
    exito = (False, "")
    if not request.user.is_authenticated():
        logout(request)
        return redirect('/')

    administrador = Administrador.objects.filter(usuario__usuario=request.user)[0]

    if request.method == "POST":
        form = request.POST
        titulo = form.get("titulo")
        descripcion = form.get("contenido")
        imagen = request.FILES.get("imagen")

        noticia = Noticia(titulo=titulo, descripcion=descripcion, imagen=imagen, administrador=administrador)
        noticia.save()

        exito = (True, "La noticia fue creada correctamente")

    template = loader.get_template('administrador/new_notice.html')
    ctx = {
        "nombre": administrador.usuario.nombre.title(),
        "exito": exito,
    }
    return HttpResponse(template.render(ctx, request))

def deactivateAdministrador(request):
    if not request.user.is_authenticated():
        logout(request)
        return redirect('/')

    administrador = Administrador.objects.filter(usuario__usuario=request.user)[0]

    if request.method=="POST" and "eliminar" in request.POST:
        administrador.estadoCuenta = False
        administrador.save()
        return redirect('/cuentaEliminada')

    suscriptores = Suscriptor.objects.filter(administrador=administrador)
    eliminar = True
    print(suscriptores)
    for suscriptor in suscriptores:
        print(eliminar, suscriptor.estadoCuenta)
        if suscriptor.estadoCuenta:
            eliminar = False
    print(eliminar)
    template = loader.get_template('administrador/desactivar_cuenta.html')
    ctx = {
        'eliminar': eliminar,
    }
    return HttpResponse(template.render(ctx, request))
