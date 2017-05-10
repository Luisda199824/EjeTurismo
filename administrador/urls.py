from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', indexAdmin),
    url(r'^modificar/perfil/$', modificarPerfilAdmin),
    url(r'^solicitudes/$', solicitudesAdmin),
    url(r'^apply/(?P<id_solicitud>(\d+))$', applySolicitudAdmin),
    url(r'^remove/(?P<id_solicitud>(\d+))$', removeSolicitudAdmin),
    url(r'^new/notice$', newNotice),
]
