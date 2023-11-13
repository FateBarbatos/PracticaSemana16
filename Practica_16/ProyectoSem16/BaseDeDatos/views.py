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
    carreras = list(Carreras.objects.all())
    doc_externo = loader.get_template('Carreras.html')
    documento = doc_externo.render({"objetos":carreras})
    return HttpResponse(documento)

def profesores(request):
    profesores = list(Profesores.objects.all())
    doc_externo = loader.get_template('Profesores.html')
    documento = doc_externo.render({'objetos':profesores})
    return HttpResponse(documento)

def estudiantes(reques):
    estudiantes = list(Estudiantes.objects.all())
    doc_externo = loader.get_template('Estudiantes.html')
    documento = doc_externo.render({'objetos':estudiantes})
    return HttpResponse(documento)

def asignaturas(request):
    asignaturas = list(Asignaturas.objects.all())
    doc_externo = loader.get_template('Asignaturas.html')
    documento = doc_externo.render({'objetos':asignaturas})
    return HttpResponse(documento)