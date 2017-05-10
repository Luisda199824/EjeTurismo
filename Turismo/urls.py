from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('iniciarSesion.urls', namespace="Iniciar sesion")),
    url(r'^', include('iniciarSesionRoot.urls', namespace="Iniciar sesion Root")),
    url(r'^', include('registroUsuarios.urls', namespace="Registro Usuario")),
    url(r'^', include('recuperarPassword.urls', namespace="recuperarPassword")),
    url(r'^suscriptor/', include('suscriptor.urls', namespace="Usuario Suscriptor")),
    url(r'^administrador/', include('administrador.urls', namespace="Usuario Administrador")),
    url(r'^root/', include('root.urls', namespace="Usuario Root")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
