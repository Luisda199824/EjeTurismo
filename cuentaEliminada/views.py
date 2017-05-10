from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

def cuentaEliminada(request):
    template = loader.get_template('cuentaEliminada/index.html')
    ctx = {}
    return HttpResponse(template.render(ctx, request))
