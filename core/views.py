from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Campus, Division, Servicio
from django.http import HttpResponseRedirect


def home_page(request):
    return render(request, 'core/home_page.html')

def lista_campus(request):
    campuss = Campus.objects.all()
    return render(request, 'core/lista_campus.html', {'campuss': campuss})

def lista_divisiones(request, pk):
    divisiones = Division.objects.all().filter(campus_id=pk)
    return render(request, 'core/lista_divisiones.html', {'divisiones': divisiones})

def lista_servicios(request, pk):
    servicios = Servicio.objects.all().filter(divisiones__id=pk)
    print(servicios)
    return render(request, 'core/lista_servicios.html', {'servicios': servicios})

def info_servicios(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    return render(request, 'core/info_servicio.html', {'servicio': servicio})

def mis_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'core/mis_servicios.html', {'servicios': servicios})

def nuevo_servicio(request):
    return render(request, 'core/nuevo_servicio.html')