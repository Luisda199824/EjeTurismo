from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, authenticate, logout

from modelsAdmin.models import Usuario, Administrador, Suscriptor, ListaSolicitudesSuscriptor, ListaSolicitudesAdministrador, Root, Municipio
from django.contrib.auth.models import User

def registerUsuario(request):
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
        genero = form.get("genero")
        pais = form.get("pais")
        password = form.get("password")
        municipio = form.get("municipio")
        municipio_admin = form.get("municipio_admin")

        len_nombre = len(nombre)
        len_apellido = len(apellido)
        len_dni = len(dni)
        len_direccion = len(direccion)
        len_telefono = len(telefono)
        len_email = len(email)
        len_genero = len(genero)
        len_pais = len(pais)
        len_password = len(password)
        len_municipio = len(municipio)
        len_municipio_admin = len(municipio_admin)

        if (len_nombre*len_apellido*len_dni*len_direccion*len_telefono*len_email*len_genero*len_pais*len_password*len_municipio) == 0:
            error = (True, "Debe ingresar todos los campos")
        elif "btn_administrador" in form and len_municipio_admin == 0:
            error = (True, "Para ser administrador, debes seleccionar un municipio que administrar")
        else:
            if len(password) <= 8:
                error = (True, "La contraseña debe contener más de 8 digitos")
            else:
                administrador = Administrador.objects.all()

                if len(administrador) == 0:
                    error = (True, "Actualmente no se encuentran administradores disponibles")
                else:
                    administrador = administrador[0]

                if len(User.objects.filter(username=email.lower())) > 0:
                    error = (True, "El correo ya ha sido usado")
                else:
                    municipio = Municipio.objects.filter(id=municipio)[0]

                    user = User(username=email.lower(), password=password)
                    user.save()

                    user.set_password(password)
                    user.save()
                    from datetime import datetime

                    usuario = Usuario(
                        dni=dni,
                        nombre=nombre,
                        apellido=apellido,
                        direccion=direccion,
                        telefono=telefono,
                        ciudad=municipio.nombre,
                        email=email,
                        genero=genero,
                        pais=pais,
                        usuario=user,
                        fecha_nacimiento=datetime.now(),
                    )

                    usuario.save()

                    municipio = Municipio.objects.filter(id=municipio_admin)[0]
                    if "btn_usuario" in form:
                        administrador = Administrador.objects.filter(municipio=municipio)
                        if len(administrador) == 0:
                            error = (True, 'Aún no existe un administrador para este municipio, ¡Sé tu!')
                        else:
                            administrador = administrador[0]
                            suscrito = Suscriptor(administrador=administrador, usuario=usuario, estadoCuenta=False)
                            suscrito.save()
                            solicitud = ListaSolicitudesSuscriptor(suscriptor=suscrito, evaluada=False)
                            solicitud.save()
                            exito = (True, "Usuario suscriptor creado, solicitud enviada")
                    elif "btn_administrador" in form:
                        administradores = Administrador.objects.filter(municipio=municipio)
                        if len(administradores) != 0:
                            error = (True, "Ya hay un administrador para el municipio de " + municipio.nombre)
                        else:
                            admin = Administrador(usuario=usuario, estadoCuenta=False, municipio=municipio, root=Root.objects.all()[0])
                            admin.save()
                            solicitud = ListaSolicitudesAdministrador(administrador=admin, evaluada=False)
                            solicitud.save()
                            exito = (True, "Usuario administrador creado, solicitud enviada")

    municipios = []
    for administrador in Administrador.objects.all():
        municipios.append(administrador.municipio)

    template = loader.get_template('registroUsuarios/index.html')
    ctx = {
        'error': error,
        'exito': exito,
        'municipios': municipios,
        'municipios_all': Municipio.objects.all(),
    }
    return HttpResponse(template.render(ctx, request))
