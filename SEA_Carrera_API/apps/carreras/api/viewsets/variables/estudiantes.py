from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from apps.carreras.models import *
from rest_framework import viewsets
from django.db.models import Count



class ProtagonismoView(viewsets.ViewSet):
    def list(self, request):
        # Obtener la lista de IDs de los estudiantes involucrados en proyectos comunitarios
        estudiantes_comunitarios = Comunitario.objects.filter(idEstudiante__isnull=False).values_list('idEstudiante', flat=True).distinct()

        # Obtener la lista de IDs de los estudiantes involucrados en proyectos de extensión
        estudiantes_extensionistas = Extensionista.objects.filter(idEstudiante__isnull=False).values_list('idEstudiante', flat=True).distinct()

        # Combinar las dos listas de IDs de estudiantes
        estudiantes_involucrados = list(estudiantes_comunitarios) + list(estudiantes_extensionistas)

        # Obtener la cantidad total de estudiantes
        total_estudiantes = Estudiante.objects.count()

        # Calcular el porcentaje de estudiantes involucrados
        porcentaje = len(set(estudiantes_involucrados)) * 100 / total_estudiantes

        # Verificar si el porcentaje es mayor al 90%
        if porcentaje > 90:
            resultado = "protagonismo"
        else:
            resultado = "no protagonismo"

        # Crear el diccionario de respuesta
        response_data = {
            "estudiantes_involucrados": len(set(estudiantes_involucrados)),
            "total_estudiantes": total_estudiantes,
            "porcentaje_involucrados": porcentaje,
            "resultado": resultado,
        }

        return Response({'resultado': response_data})

