from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', indexAdmin),
    url(r'^modificar/perfil/$', modificarPerfilAdmin),
    url(r'^solicitudes/$', solicitudesAdmin),
    url(r'^apply/(?P<id_solicitud>(\d+))$', applySolicitudAdmin),
    url(r'^remove/(?P<id_solicitud>(\d+))$', removeSolicitudAdmin),
    url(r'^noticias/$', noticiasAdministrador),
    url(r'^new/notice/$', newNotice),
    url(r'^noticias/modify/(?P<id_noticia>(\d+))/$', modifyNoticiaAdmin),
    url(r'^noticias/delete/(?P<id_noticia>(\d+))/$', deleteNoticiaAdmin),
    url(r'^deactivate$', deactivateAdministrador),
    
]
