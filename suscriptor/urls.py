from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', indexSuscriptor),
    url(r'^deactivate$', deactivateSuscriptor),
]
