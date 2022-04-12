from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.


class MyLoginView(LoginView):
   success_url = '/'
   
   def form_invalid(self, form):
    return render('/')

   def form_valid(self, form):
    auth_login(self.request, form.get_user())
    return HttpResponseRedirect('/')



class MySignupView(CreateView):
   form_class = UserCreationForm
   success_url = '/accounts/login'
   template_name = 'registration/signup.html'



