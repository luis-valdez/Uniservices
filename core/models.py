from django.db import models
from django.conf import settings
from django.utils import timezone


class Campus(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(null=False, blank=False)

    def __str__(self):
	    return self.nombre

class Division(models.Model):
    id = models.IntegerField(primary_key=True)
    id_campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField()

