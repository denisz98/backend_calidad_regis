from django.urls import path
from .download import *


urlpatterns = [
    
    path('alumno_ayudante/<int:pk>/<str:attribute>/', download_files_Alumno_ayudante, name='download_files_Alumno_ayudante'),
    path('departamento/<int:pk>/<str:attribute>/', download_files_Departamento, name='download_files_Departamento'),
    path('carrera/<int:pk>/<str:attribute>/', download_files_Carrera, name='download_files_Carrera'),
    path('disciplina/<int:pk>/<str:attribute>/', download_files_Disciplina, name='download_files_Disciplina'),
    path('expediente/<int:pk>/<str:attribute>/', download_files_Expediente, name='download_files_Expediente'),
    path('laboratorio/<int:pk>/<str:attribute>/', download_files_Laboratorio, name='download_files_Laboratorio'),
    path('posgrado/<int:pk>/<str:attribute>/', download_files_Posgrado, name='download_files_Posgrado'),
    path('trabajo_diploma/<int:pk>/<str:attribute>/', download_files_Trabajo_diploma, name='download_files_Trabajo_diploma'),
    path('catedra_honorifica/<int:pk>/<str:attribute>/', download_files_Catedra_honorifica, name='download_files_Catedra_honorifica'),
    path('comunitario/<int:pk>/<str:attribute>/', download_files_Comunitario, name='download_files_Comunitario'),
    path('extensionista/<int:pk>/<str:attribute>/', download_files_Extensionista, name='download_files_Extensionista'),
    path('investigacion/<int:pk>/<str:attribute>/', download_files_Investigacion, name='download_files_Investigacion'),
    path('asignatura/<int:pk>/<str:attribute>/', download_files_Asignatura, name='download_files_Asignatura'),
    path('ejercicio_integrador/<int:pk>/<str:attribute>/', download_files_Ejercicio_integrador, name='download_files_Ejercicio_integrador'),
    path('egresado/<int:pk>/<str:attribute>/', download_files_Egresado, name='download_files_Egresado'),

]
