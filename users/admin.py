# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


from .models import Usuario, Encargado_Servicio

class CustomUserAdmin(UserAdmin):
    model = Usuario
admin.site.register(Usuario, CustomUserAdmin)


admin.site.register(Encargado_Servicio)