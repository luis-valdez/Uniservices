# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


from .models import Usuario

class CustomUserAdmin(UserAdmin):
    model = Usuario
admin.site.register(Usuario, CustomUserAdmin)