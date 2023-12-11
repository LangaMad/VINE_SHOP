from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.views.generic import TemplateView,FormView,CreateView

# from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import *
# Create your views here.
class RegisterView(CreateView):
    template_name ='register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('index')
