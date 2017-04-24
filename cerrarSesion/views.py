from django.shortcuts import redirect

from django.contrib.auth import logout

def indexLogout(request):
    logout(request)
    return redirect('/')
