from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('iniciarSesion.urls', namespace="Iniciar sesion")),
    url(r'^', include('iniciarSesionRoot.urls', namespace="Iniciar sesion Root")),
    url(r'^', include('registroUsuarios.urls', namespace="Registro Usuario")),
    url(r'^suscriptor/', include('suscriptor.urls', namespace="Usuario Suscriptor")),
]
