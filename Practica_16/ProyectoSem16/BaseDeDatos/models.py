from django.db import models

# Create your models here.


#Tabla de carreras
class Carreras(models.Model):
    Nombre_Carrera = models.TextField()

#Tabla de profesores
class Profesores(models.Model):
    Nombre_profesores = models.TextField()
    Apellido_profesores = models.TextField()
    Correo_profesores = models.TextField()

#Tabla de estudiantes
class Estudiantes(models.Model):
    Nombre_estudiante = models.TextField()
    Apellido_estudiante = models.TextField()
    Edad_estudiante = models.TextField()
    Carrera_estudiante = models.ForeignKey(Carreras,on_delete=models.CASCADE)

#Tabla de asignatura
class Asignaturas(models.Model):
    Nombre_asignatura = models.TextField()
    Profesor_asignatura = models.ForeignKey(Profesores,on_delete=models.CASCADE)
    Carrera_asignatura = models.ForeignKey(Carreras,on_delete=models.CASCADE)