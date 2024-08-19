from django.shortcuts import redirect
from django.urls import reverse




def authorise(view_fun):
    def wrapper_fun(request,*args,**kwargs):
        if request.user.is_authenticated:
            redirectTo = reverse('home',kwargs={'pk':request.user.id})
            return redirect(redirectTo)
        else:
            return view_fun(request,*args,**kwargs)
        
    return wrapper_fun


