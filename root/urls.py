from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', indexRoot),
    url(r'^modificar/perfil/$', modificarPerfilRoot),
    url(r'^solicitudes/$', solicitudesRoot),
    url(r'^apply/(?P<id_solicitud>(\d+))$', applySolicitudRoot),
    url(r'^remove/(?P<id_solicitud>(\d+))$', removeSolicitudRoot),
]
