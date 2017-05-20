from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', mapsIndex),
    url(r'^delete/marker/(?P<id_marker>(\d+))$', deleteMarker),
    url(r'^modify/marker/(?P<id_marker>(\d+))$', modifyMarker),
]
