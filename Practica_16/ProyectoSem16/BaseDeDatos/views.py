from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Carreras,Profesores,Asignaturas,Estudiantes
from django.template import Context,loader


# Create your views here.'

#clase para crear la tabla

#View para la tabla de carreras
def index(reques):
    doc_externo = loader.get_template('index.html')
    documento = doc_externo.render()
    return HttpResponse(documento)

def carreras(request):
    carreras = list(Carreras.objects.values())
    doc_externo = loader.get_template('Carreras.html')
    documento = doc_externo.render({"objetos":carreras})
    return HttpResponse(documento)

def profesores(request):
    profesores = list(Profesores.objects.values())
    doc_externo = loader.get_template('Profesores.html')
    documento = doc_externo.render({'objetos':profesores})
    return HttpResponse(documento)

def estudiantes(reques):
    estudiantes = list(Estudiantes.objects.values())
    return JsonResponse(estudiantes,safe=False)

def asignaturas(request):
    asignaturas = list(Asignaturas.objects.values())
    return JsonResponse(asignaturas,safe=False)