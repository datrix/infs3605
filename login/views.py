from django.http import HttpResponse 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login #verifies username and password 
from .forms import UserForm 
from django.views.generic import View
from django.template import loader
from django.contrib.auth.views import login
from django.contrib.auth.views import logout


def index(request):
  return HttpResponse("<h1>Login/homepage</h1>")

def test(request):
  return HttpResponse("<h1>Login Successful</h1>")

class UserFormView(View):
  form_class = UserForm
  template_name = 'login.html'

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                redirect_to = settings.LOGIN_REDIRECT_URL
                return render(request, url=redirect_to, host=request.get_host()) 
                
            else:
                return render(request, 'login/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login/login.html', {'error_message': 'Invalid login'})
    return render(request, 'login/login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")
  
  