from django.db import models
from django.conf import settings
from django.utils import timezone

class Campus(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(null=False, blank=False)

    def __str__(self):
	    return self.nombre

class Division(models.Model):
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(null=False, blank=False)

class Servicio(models.Model):
    divisiones = models.ManyToManyField(Division)
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    duracion = models.IntegerField()
    capacidad = models.IntegerField()
    imagen = models.ImageField(null=False, blank=False)



