from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from modelsAdmin.models import Usuario, Administrador, Suscriptor, Marcador

def mapsIndex(request):
	exito = (False, '')
	if request.user is None:
		return redirect('/')

	type_user = ""
	usuario = Usuario.objects.filter(usuario=request.user)
	user = None
	if len(usuario) == 0:
		return redirect('/')
	else:
		usuario = usuario[0]
		admin = Administrador.objects.filter(usuario=usuario)
		
		if len(admin) == 0:
			suscrito = Suscriptor.objects.filter(usuario=usuario)
			if len(suscrito) == 0:
				return redirect('/')
			else:
				type_user = "suscrito"
				user = suscrito[0]
		else:
			type_user = "administrador"
			user = admin[0]

	if request.method == "POST":
		form = request.POST
		lat = form.get("latitud")
		lng = form.get("longitud")
		titulo = form.get("titulo")
		contenido = form.get("contenido")
		marker = Marcador(titulo=titulo, descripcion=contenido, latitud=lat, longitud=lng, usuario=usuario)
		marker.save()
		exito = (True, "Marcador guardado")

	marcadores = Marcador.objects.all()
	template = loader.get_template('maps/index.html')
	ctx = {
		'nombre': user.usuario.nombre.title() + " " + user.usuario.apellido.title(),
		'type_user': type_user,
		'exito': exito,
		'marcadores': marcadores,
		'id_usuario': usuario.id,
	}
	return HttpResponse(template.render(ctx, request))

def modifyMarker(request, id_marker):
	if request.user is None:
		return redirect('/')

	type_user = ""
	usuario = Usuario.objects.filter(usuario=request.user)
	user = None
	if len(usuario) == 0:
		return redirect('/')
	else:
		usuario = usuario[0]
		admin = Administrador.objects.filter(usuario=usuario)
		
		if len(admin) == 0:
			suscrito = Suscriptor.objects.filter(usuario=usuario)
			if len(suscrito) == 0:
				return redirect('/')
			else:
				type_user = "suscriptor"
				user = suscrito[0]
		else:
			type_user = "administrador"
			user = admin[0]

	exito = (False, '')
	error = (False, '')
	marcador = Marcador.objects.filter(id=id_marker)
	if len(marcador) == 0:
		error = (True, "No se encuentra el marcador")
		marcador = None
	else:
		marcador = marcador[0]
		if request.method == "POST":
			form = request.POST
			lat = form.get("latitud")
			lng = form.get("longitud")
			titulo = form.get("titulo")
			contenido = form.get("contenido")
			marcador.titulo = titulo
			marcador.descripcion = contenido
			marcador.longitud = lng
			marcador.latitud = lat
			marcador.save()
			exito = (True, "Marcador actualizado correctamente")

	template = loader.get_template('maps/modify_marker.html')
	ctx = {
		'nombre': user.usuario.nombre.title() + " " + user.usuario.apellido.title(),
		'type_user': type_user,
		'exito': exito,
		'error': error,
		'marcador': marcador,
		'id_usuario': usuario.id,
	}
	return HttpResponse(template.render(ctx, request))

def deleteMarker(request, id_marker):
	if request.user is None:
		return redirect('/')

	type_user = ""
	usuario = Usuario.objects.filter(usuario=request.user)
	user = None
	if len(usuario) == 0:
		return redirect('/')
	else:
		usuario = usuario[0]
		admin = Administrador.objects.filter(usuario=usuario)
		
		if len(admin) == 0:
			suscrito = Suscriptor.objects.filter(usuario=usuario)
			if len(suscrito) == 0:
				return redirect('/')
			else:
				type_user = "suscriptor"
				user = suscrito[0]
		else:
			type_user = "administrador"
			user = admin[0]

	exito = (False, '')
	error = (False, '')
	marcador = Marcador.objects.filter(id=id_marker)
	if len(marcador) == 0:
		error = (True, "No se encuentra el marcador")
	else:
		marcador[0].delete()
		exito = (True, "El marcador ha sido eliminado correctamente")

	template = loader.get_template('maps/delete_marker.html')
	ctx = {
		'nombre': user.usuario.nombre.title() + " " + user.usuario.apellido.title(),
		'type_user': type_user,
		'exito': exito,
		'error': error,
		'id_usuario': usuario.id,
	}
	return HttpResponse(template.render(ctx, request))