from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse

def index(request):
    template = loader.get_template('landing/index.html')
    ctx = {}
    return HttpResponse(template.render(ctx, request))
