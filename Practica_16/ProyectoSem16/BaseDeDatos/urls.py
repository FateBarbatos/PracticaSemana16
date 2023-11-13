from django.urls import path
from . import views

#urls separadas para cada view
urlpatterns = [
        path('',views.index),
        path('carreras/',views.carreras),
        path('estudiantes/',views.estudiantes),
        path('asignaturas/',views.asignaturas),
        path('profesores/',views.profesores)
    ]
