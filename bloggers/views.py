from django.contrib import messages
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.shortcuts import render, redirect
from django.views import View


class LoginView(View):

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get('login_username')
        password = request.POST.get('login_password')

        authenticated_user = authenticate(username=username, password=password)
        if authenticated_user and authenticated_user.is_active:
            django_login(request, authenticated_user)
            return redirect('home')
        else:
            messages.error(request, "Usuario incorrecto o inactivo")
            return render(request, "login.html")

def logout(request):
    django_logout(request)
    return redirect("login")

