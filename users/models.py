# users/models.py
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Usuario(AbstractUser):
    es_estudiante = models.BooleanField(default=False)
    es_tutor = models.BooleanField(default=False)
    es_encargado_servicio = models.BooleanField(default=False)
  
class Tutor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    nombre = models.CharField(max_length=100)
    num_empleado = models.IntegerField()

class Estudiante(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    nombre = models.CharField(max_length=100) 
    expediente = models.IntegerField()
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)

class Encargado_Servicio(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    nombre = models.CharField(max_length=100)