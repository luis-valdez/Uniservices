from django.shortcuts import render
from .models import Image

def home_page(request):
    images = Image.objects.order_by('?').first()
    return render(request, 'core/home_page.html', {'images' : images})

def login(request):
    return render(request, 'core/inicia_sesion.html')
    