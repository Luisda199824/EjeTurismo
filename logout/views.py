from django.shortcuts import redirect
from django.contrib.auth import logout

def logout(request):
    if request.user is not None and not request.user.is_authenticated():
        logout(request)

    return redirect('/')
