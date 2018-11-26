from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Campus
from django.http import HttpResponseRedirect


def home_page(request):
    return render(request, 'core/home_page.html')

def lista_campus(request):
    campuss = Campus.objects.all()
    return render(request, 'core/lista_campus.html', {'campuss': campuss})

def lista_divisiones(request, pk):
    division = get_object_or_404(Campus, pk=pk)
    return render(request, 'core/lista_divisiones', {'division': division})