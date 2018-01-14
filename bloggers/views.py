from django.contrib import messages
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from bloggers.forms import LoginForm, SignUpForm


class LoginView(View):

    def get(self, request):
        context = {'form': LoginForm()}
        return render(request, "login.html", context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data.get('login_username')
            password = form.cleaned_data.get('login_password')

            authenticated_user = authenticate(username=username, password=password)
            if authenticated_user and authenticated_user.is_active:
                django_login(request, authenticated_user)
                redirect_to = request.GET.get("next", "home")
                return redirect(redirect_to)
            else:
                messages.error(request, "Usuario incorrecto o inactivo")
        return render(request, "login.html", {'form': form})

def logout(request):
    django_logout(request)
    return redirect("login")

class AuthorView(ListView):
    model = User
    template_name = "blogs_authors.html"

    def get_queryset(self):
        queryset = super(AuthorView, self).get_queryset()
        return queryset.order_by('username')

class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

    def post(self,request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            authenticated_user = authenticate(username=username, password=raw_password)
            django_login(request, authenticated_user)
            return redirect('home')
