
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from apps.carreras.models import *
import os

def download_file(request, model, pk, attribute):
    print('model', model)
    print('pk', pk)
    print('attribute', attribute)
    try:
        obj = model.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return HttpResponse('El archivo no existe', status=404)

    # Verifica si el archivo adjunto existe en el sistema de archivos
    attr = getattr(obj, attribute)
    if not attr or not attr.path or not os.path.exists(attr.path):
        return HttpResponse('El archivo no existe', status=404)

    # Define el nombre del archivo
    filename = os.path.basename(attr.path)

    # Lee el archivo en modo binario
    with open(attr.path, 'rb') as f:
        # Crea una respuesta HTTP con el contenido del archivo
        response = HttpResponse(content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename={filename}'

        # Agrega el contenido del archivo a la respuesta HTTP
        response.write(f.read())

    return response


# ===============================================================Alumno_ayudante=======================================================================#

def download_files_Alumno_ayudante(request, pk, attribute):
    return download_file(request, Alumno_ayudante, pk, attribute)


# ===============================================================Carrera=======================================================================#


def download_files_Carrera(request, pk, attribute):
    return download_file(request, Carrera, pk, attribute)

# ===============================================================Departamento=======================================================================#


def download_files_Departamento(request, pk, attribute):
    return download_file(request, Departamento, pk, attribute)

# ===============================================================Disciplina=======================================================================#


def download_files_Disciplina(request, pk, attribute):
    return download_file(request, Disciplina, pk, attribute)

# ===============================================================Expediente=======================================================================#


def download_files_Expediente(request, pk, attribute):
    return download_file(request, Expediente, pk, attribute)

# ===============================================================Laboratorio=======================================================================#


def download_files_Laboratorio(request, pk, attribute):
    return download_file(request, Laboratorio, pk, attribute)
# ===============================================================Posgrado=======================================================================#


def download_files_Posgrado(request, pk, attribute):
    return download_file(request, Posgrado, pk, attribute)

# ===============================================================Trabajo_diploma=======================================================================#


def download_files_Trabajo_diploma(request, pk, attribute):
    return download_file(request, Trabajo_diploma, pk, attribute)

# ===============================================================Catedra_honorifica=======================================================================#


def download_files_Catedra_honorifica(request, pk, attribute):
    return download_file(request, Catedra_honorifica, pk, attribute)

# ===============================================================Comunitario=======================================================================#


def download_files_Comunitario(request, pk, attribute):
    return download_file(request, Comunitario, pk, attribute)

# ===============================================================Extensionista=======================================================================#


def download_files_Extensionista(request, pk, attribute):
    return download_file(request, Extensionista, pk, attribute)

# ===============================================================Investigacion=======================================================================#


def download_files_Investigacion(request, pk, attribute):
    return download_file(request, Investigacion, pk, attribute)

# ===============================================================Asignatura=======================================================================#


def download_files_Asignatura(request, pk, attribute):
    return download_file(request, Asignatura, pk, attribute)

# ===============================================================Ejercicio_integrador=======================================================================#


def download_files_Ejercicio_integrador(request, pk, attribute):
    return download_file(request, Ejercicio_integrador, pk, attribute)
# ===============================================================Egresado=======================================================================#


def download_files_Egresado(request, pk, attribute):
    return download_file(request, Egresado, pk, attribute)

