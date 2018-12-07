from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Campus, Division, Servicio
from django.http import HttpResponseRedirect
from .forms import PostForm
from django.shortcuts import redirect


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

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('lista_campus')
    else:
        form = PostForm()
    return render(request, 'core/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Campus)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('lista_campus')
    else:
        form = PostForm(instance=post)
    return render(request, 'core/post_edit.html', {'form': form})