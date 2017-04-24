from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def iniciarSesion(request):
    template = loader.get_template('iniciarSesion/index.html')
    ctx = {}
    return HttpResponse(template.render(ctx, request))
