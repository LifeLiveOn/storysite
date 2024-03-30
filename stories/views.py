from django.contrib.auth import logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm

User = get_user_model()


# Create your views here.
def index(request):
    return None


def about(request):
    return None


def contact(request):
    return None


def login(request):
    return None


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


@login_required
def story(request):
    pass


@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse_lazy("home"))
