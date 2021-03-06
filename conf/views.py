from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

# Create your views here.


class MyLoginView(LoginView):
    success_url = '/'
    template_name = 'registration/login.html'


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = '/login'
    template_name = 'registration/signup.html'
