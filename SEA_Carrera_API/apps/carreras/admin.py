from django.contrib import admin
from .models import *

# ------------------------------------------START TABLES DENIS------------------------------------------------------------
admin.site.register(Laboratorio)
admin.site.register(Estudiante)
admin.site.register(Carrera)
admin.site.register(Departamento)
admin.site.register(Datos_promocion)
admin.site.register(Egresado)
# admin.site.register(Actividad_superacion)
admin.site.register(Asignatura_virtual)
admin.site.register(Practica_laboral)
# admin.site.register(Bibliografia)
# admin.site.register(Software)
admin.site.register(Alumno_ayudante)
admin.site.register(Disciplina)
admin.site.register(Asignatura)
admin.site.register(Asignatura_ejIntegrador)
admin.site.register(Trabajo_diploma)
admin.site.register(Trab_diploma_profesor_estudiante)
admin.site.register(Proyecto)
admin.site.register(Investigacion)
admin.site.register(Extensionista)
admin.site.register(Comunitario)
admin.site.register(Catedra_honorifica)
admin.site.register(Ejercicio_integrador)
admin.site.register(Asignatura_profesor)
# # ------------------------------------------END TABLES DENIS------------------------------------------------------------
# # ------------------------------------------START TABLES HECTOR------------------------------------------------------------
admin.site.register(Publicacion)
admin.site.register(Libro)
admin.site.register(Revista)
admin.site.register(Trabajador)
admin.site.register(Profesor)
admin.site.register(Profesor_disciplina)
admin.site.register(Profesor_cargo_metodologico)
admin.site.register(Profesor_posgrado)
admin.site.register(Cargo_metodologico)
admin.site.register(Trabajador_no_docente)
admin.site.register(Premio)
# # ------------------------------------------END TABLES HECTOR------------------------------------------------------------
# # ------------------------------------------START TABLES LIETIS------------------------------------------------------------
admin.site.register(Ponencia_evento)
admin.site.register(Estudiante_posgrado)
admin.site.register(Posgrado)
admin.site.register(Expediente)
# ------------------------------------------END TABLES LIETIS------------------------------------------------------------
