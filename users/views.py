# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView, CreateView
from .models import Usuario, Estudiante, Tutor
from django.shortcuts import redirect, render
#from .forms import StudentSignUpForm, TutorSignUpForm
from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
'''
class EstudianteSignUpView(CreateView):
    model = Usuario
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('')

class TutorSignUpView(CreateView):
    model = Usuario
    form_class = TutorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'tutor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('')
'''