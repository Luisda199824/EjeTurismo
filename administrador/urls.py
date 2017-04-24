from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', indexAdmin),
    url(r'^modificar/perfil/$', modificarPerfilAdmin),
]
