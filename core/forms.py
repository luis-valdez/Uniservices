from django import forms
from .models import Division


class Service(forms.Form):
    nombre = forms.CharField(label='nombre',max_length=100)
    ubicacion = forms.CharField(label='ubicacion',max_length=100)
    descripcion = forms.CharField(label='descripcion',max_length=100)
    duracion = forms.DurationField(label='duracion')
    capacidad = forms.IntegerField(label='capacidad',min_value=1)
    imagen = forms.ImageField(label='imagen')
