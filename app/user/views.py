from django.contrib.auth.views import LoginView
from django.shortcuts import render


class SignInView(LoginView):
    template_name = "login.html"
