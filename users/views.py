# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView, CreateView
from .models import Usuario, Estudiante, Tutor
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'