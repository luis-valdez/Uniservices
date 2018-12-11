from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Campus, Division, Servicio
from django.http import HttpResponseRedirect
from users.models import Usuario, Estudiante, Tutor, Encargado_Servicio
from .forms import Service


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

def mi_tutor(request):
    usuario = request.user
    estudiante = usuario.estudiante
    tutor = Tutor.objects.filter(estudiante=estudiante).first()
    usuario_tutor = Usuario.objects.filter(tutor=tutor).first()
    return render(request, 'core/mi_tutor.html', {'tutor': tutor, 'usuario_tutor' : usuario_tutor})

def mis_alumnos(request):
    usuario = request.user
    tutor = usuario.tutor
    estudiantes = Estudiante.objects.filter(tutor=tutor)
    return render(request, 'core/mis_alumnos.html', {'estudiantes': estudiantes})

def agendar_citas(request):
    return render(request, 'core/calendar.html')

def mis_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'core/mis_servicios.html', {'servicios': servicios})

def nuevo_servicio(request):
    form = Service
    servicios = Servicio.objects.all()
    if request.method == 'POST':
        form2 = Service(request.POST, request.FILES or None)
        if form2.is_valid():
            nomb = form2.data.get("nombre")
            ubic = form2.data.get("ubicacion")
            desc = form2.data.get("descripcion")
            dura = form2.data.get("duracion")
            capa = form2.data.get("capacidad")
            imag = request.FILES["imagen"]
            usr = request.user
            encser = Encargado_Servicio.objects.filter(usuario=usr).first()
            div = encser.division
            newServ = Servicio(nombre=nomb, ubicacion=ubic, descripcion=desc, duracion=dura, capacidad=capa, imagen=imag, encargado=usr)
            newServ.save()
            newServ.divisiones.add(div)
            return render(request, 'core/mis_servicios.html', {'servicios': servicios})
    else:
        return render(request, 'core/nuevo_servicio.html', {'form' : form})
