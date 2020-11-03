from django.http import HttpResponse
from  django.shortcuts import redirect
from django.contrib.auth.models import Group

def unauth_user(veiw_func):
    def wrapped(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return veiw_func(request,*args,**kwargs)
    return wrapped

def allowed_users(allowed_rolers=[]):
    def decorator(view_func):
        def wrapped(request,*args,**kwargs):
            group = None
            if request.user.groups.all():
                group = request.user.groups.all()[0].name
            if group in allowed_rolers:
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse('you have no permissions')
        return wrapped
    return decorator

def admin_only(view_func):
    def wrapped(request,*args,**kwargs):
        group = None
        if request.user.groups.all():
            group = request.user.groups.all()[0].name
        if group == 'Costomer':
            return redirect('user')
        if group == 'manager':
            return view_func(request, *args, **kwargs)
    return wrapped