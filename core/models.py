from django.db import models
from django.conf import settings
from django.utils import timezone
from users.models import Usuario

class Campus(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(null=False, blank=False)

    def __str__(self):
	    return self.nombre

class Division(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(null=False, blank=False)

class Servicio(models.Model):
    divisiones = models.ManyToManyField(Division)
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    duracion = models.DurationField()
    capacidad = models.IntegerField()
    imagen = models.ImageField(null=False, blank=False)
    encargado = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=0)