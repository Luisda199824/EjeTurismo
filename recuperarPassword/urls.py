from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^reset/password$', resetPassword),
    url(r'^new/password/?P<hash>[0-9]+$', changePasswordWithHash),
]
