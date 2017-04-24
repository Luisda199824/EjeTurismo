from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, authenticate, logout

from modelsAdmin.models import Usuario, Administrador, Suscriptor, ListaSolicitudesSuscriptor, ListaSolicitudesAdministrador, Root
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
        ciudad = form.get("ciudad")
        genero = form.get("genero")
        pais = form.get("pais")
        password = form.get("password")
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
        len_password = len(password)
        len_municipio = len(municipio)

        if (len_nombre*len_apellido*len_dni*len_direccion*len_telefono*len_email*len_ciudad*len_genero*len_pais*len_password) == 0:
            error = (True, "Debe ingresar todos los campos")
        else:
            if "btn_administrador" in form and (len(municipio) == 0):
                error = (True, "Seleccione un municipio")
            else:
                administrador = Administrador.objects.all()

                if len(administrador) == 0:
                    error = (True, "Actualmente no se encuentran administradores disponibles")
                else:
                    administrador = administrador[0]

                if len(User.objects.filter(username=email)) > 0:
                    error = (True, "El correo ya ha sido usado")
                else:
                    user = User(username=email, password=password)
                    user.save()
                    print(password, user.password)

                    from datetime import datetime

                    usuario = Usuario(
                        dni=dni,
                        nombre=nombre,
                        apellido=apellido,
                        direccion=direccion,
                        telefono=telefono,
                        ciudad=ciudad,
                        email=email,
                        genero=genero,
                        pais=pais,
                        usuario=user,
                        fecha_nacimiento=datetime.now(),
                    )

                    usuario.save()

                    if "btn_usuario" in form:
                        suscrito = Suscriptor(administrador=administrador, usuario=usuario, estadoCuenta=False)
                        suscrito.save()
                        solicitud = ListaSolicitudesSuscriptor(suscriptor=suscrito, evaluada=False)
                        solicitud.save()
                        exito = (True, "Usuario suscriptor creado, solicitud enviada")
                    elif "btn_administrador" in form:
                        admin = Administrador(usuario=usuario, estadoCuenta=False, municipio=municipio, root=Root.objects.all()[0])
                        admin.save()
                        solicitud = ListaSolicitudesAdministrador(administrador=admin, evaluada=False)
                        solicitud.save()
                        exito = (True, "Usuario administrador creado, solicitud enviada")

    template = loader.get_template('registroUsuarios/index.html')
    ctx = {
        'error': error,
        'exito': exito,
    }
    return HttpResponse(template.render(ctx, request))
