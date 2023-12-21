from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import authenticate
from django.views.generic import CreateView, FormView
from django.urls import reverse_lazy
from django.http import HttpResponse
from rest_framework import generics

from .models import User
from .serilizers import UserSetializer


class RegisterView(CreateView):
    template_name ='register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('index')

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        username = data['username']
        email = data['email']
        password = data['password1']
        user = authenticate(username=username, email=email,
        password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('index')
            else:
                return HttpResponse('Ваш аккаунт забанен')
        return HttpResponse('Такого юзера не существует')


def UserLogout(request):
    if request.user.is_authenticated:
        logout(request)




class UserAPIListVIew(generics.ListAPIView):
    serializer_class = UserSetializer
    context_object_name = 'user'
    queryset = User.objects.all()





