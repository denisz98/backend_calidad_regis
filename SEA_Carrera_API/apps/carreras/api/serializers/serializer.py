from apps.carreras.models import *
from .BaseSerializer import CustomSerializer
from rest_framework import serializers


class LaboratorioSerializer(CustomSerializer):
    class Meta:
        model = Laboratorio
        fields = '__all__'
    file_fields = ['disp_tecnica']


class EstudianteSerializer(CustomSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'


class CarreraSerializer(CustomSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'
        
    file_fields = ['plan_trabajo_metodologico','plan_estudio','estrategia_curricular','estrategia_educativa_carrera','estrategia_educativa_agno']



class Alumno_ayudanteSerializer(CustomSerializer):
    class Meta:
        model = Alumno_ayudante
        fields = '__all__'
    file_fields = ['plan']



class DepartamentoSerializer(CustomSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'
        
    file_fields = ['plan_trabajo_metodologico']


class DisciplinaSerializer(CustomSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'
    
    file_fields = ['plan_trabajo_metodologico']


class Datos_promocionSerializer(CustomSerializer):
    class Meta:
        model = Datos_promocion
        fields = '__all__'


class EgresadoSerializer(CustomSerializer):
    class Meta:
        model = Egresado
        fields = '__all__'
    file_fields = ['acciones_seguimiento']


class Asignatura_virtualSerializer(CustomSerializer):
    class Meta:
        model = Asignatura_virtual
        fields = '__all__'


class Practica_laboralSerializer(CustomSerializer):
    class Meta:
        model = Practica_laboral
        fields = '__all__'


# class BibliografiaSerializer(CustomSerializer):
#     class Meta:
#         model = Bibliografia
#         fields = '__all__'


# class SoftwareSerializer(CustomSerializer):
#     class Meta:
#         model = Software
#         fields = '__all__'


class AsignaturaSerializer(CustomSerializer):
    class Meta:
        model = Asignatura
        fields = '__all__'
    file_fields = ['programa']


class ProyectoSerializer(CustomSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'


class Trabajo_diplomaSerializer(CustomSerializer):
    class Meta:
        model = Trabajo_diploma
        fields = '__all__'
    file_fields = ['informe','aval']


class ExtensionistaSerializer(CustomSerializer):
    class Meta:
        model = Extensionista
        fields = '__all__'
    file_fields = ['tareas_impacto','tareas_extensionista']


class InvestigacionSerializer(CustomSerializer):
    class Meta:
        model = Investigacion
        fields = '__all__'
    file_fields = ['tareas_impacto']


class ComunitarioSerializer(CustomSerializer):
    class Meta:
        model = Comunitario
        fields = '__all__'
    file_fields = ['tareas_impacto','tareas_comunitario']

class Catedra_honorificaSerializer(CustomSerializer):
    class Meta:
        model = Catedra_honorifica
        fields = '__all__'
    file_fields = ['tareas_impacto','tareas_catedra_honorifica']


class Ejercicio_integradorSerializer(CustomSerializer):
    class Meta:
        model = Ejercicio_integrador
        fields = '__all__'
    file_fields = ['informe']


class Asignatura_ejIntegradorSerializer(CustomSerializer):
    class Meta:
        model = Asignatura_ejIntegrador
        fields = '__all__'


class Trab_diploma_profesor_estudianteSerializer(CustomSerializer):
    class Meta:
        model = Trab_diploma_profesor_estudiante
        fields = '__all__'




class Asignatura_profesorSerializer(CustomSerializer):
    class Meta:
        model = Asignatura_profesor
        fields = '__all__'


# # ------------------------------------------START TABLES HECTOR------------------------------------------------------------

class PublicacionSerializer(CustomSerializer):
    class Meta:
        model = Publicacion
        fields = '__all__'


class LibroSerializer(CustomSerializer):
    class Meta:
        model = Libro
        fields = '__all__'


class RevistaSerializer(CustomSerializer):
    class Meta:
        model = Revista
        fields = '__all__'


class TrabajadorSerializer(CustomSerializer):
    class Meta:
        model = Trabajador
        fields = '__all__'


class ProfesorSerializer(CustomSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'


class Profesor_posgradoSerializer(CustomSerializer):
    class Meta:
        model = Profesor_posgrado
        fields = '__all__'
    


class Cargo_metodologicoSerializer(CustomSerializer):
    class Meta:
        model = Cargo_metodologico
        fields = '__all__'


class Profesor_cargo_metodologicoSerializer(CustomSerializer):
    class Meta:
        model = Profesor_cargo_metodologico
        fields = '__all__'


class Trabajador_no_docenteSerializer(CustomSerializer):
    class Meta:
        model = Trabajador_no_docente
        fields = '__all__'


class Profesor_disciplinaSerializer(CustomSerializer):
    class Meta:
        model = Profesor_disciplina
        fields = '__all__'




class PremioSerializer(CustomSerializer):
    class Meta:
        model = Premio
        fields = '__all__'


# # ------------------------------------------END TABLES HECTOR------------------------------------------------------------
# # ------------------------------------------START TABLES LIETIS------------------------------------------------------------

class Ponencia_eventoSerializer(CustomSerializer):
    class Meta:
        model = Ponencia_evento
        fields = '__all__'


class Estudiante_posgradoSerializer(CustomSerializer):
    class Meta:
        model = Estudiante_posgrado
        fields = '__all__'


class PosgradoSerializer(CustomSerializer):
    class Meta:
        model = Posgrado
        fields = '__all__'
    
    file_fields = ['programa','encuesta_satisfaccion']


class ExpedienteSerializer(CustomSerializer):
    class Meta:
        model = Expediente
        fields = '__all__'
    file_fields=['archivo']

# # ------------------------------------------END TABLES LIETIS------------------------------------------------------------
