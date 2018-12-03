# users/forms.py
from django import forms
from .models import Usuario, Estudiante, Tutor
from django.db import transaction
from django.forms.utils import ValidationError
from django.contrib.auth.forms import UserCreationForm


class StudentSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Estudiante.objects.create(user=user)
        return user

class TutorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Tutor.objects.create(user=user)
        return user