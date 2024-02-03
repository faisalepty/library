from django.shortcuts import redirect
from django.http import HttpResponse


def unAuthenticated(view_func):
    def wrapper(request, *args,**kwargs):
        if request.user.is_authenticated:
            prevPage = request.META.get('HTTP_REFERER')
            return redirect(prevPage)
        else:
            return view_func(request, *args, **kwargs)
    return wrapper

def allowedUsers(allowedRoles=[]):
    def dec(view_func):
        def wrapper(request, *args, **kwargs):
            group = request.user.groups.all()[0].name
            if group in allowedRoles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorised to view this page')
        return wrapper
    return dec