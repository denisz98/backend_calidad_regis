from apps.carreras.models import *
from apps.carreras.api.serializers.serializer import *
from .BaseViewSet import GenericViewSet
from rest_framework.views import APIView
from rest_framework.response import Response


class LaboratorioViewSet(GenericViewSet):
    queryset = Laboratorio.objects.all()
    serializer_class = LaboratorioSerializer
    model = Laboratorio
    id = 'idLaboratorio'


class CarreraViewSet(GenericViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer
    model = Carrera
    id = 'idCarrera'


class Datos_promocionViewSet(GenericViewSet):
    queryset = Datos_promocion.objects.all()
    serializer_class = Datos_promocionSerializer
    model = Datos_promocion
    id = 'idDatos_promocion'


# ===================================================================================================================================================#

class EgresadoViewSet(GenericViewSet):
    queryset = Egresado.objects.all()
    serializer_class = EgresadoSerializer
    model = Egresado
    id = 'idEgresado'

# ===================================================================================================================================================#


class Asignatura_virtualViewSet(GenericViewSet):
    queryset = Asignatura_virtual.objects.all()
    serializer_class = Asignatura_virtualSerializer
    model = Asignatura_virtual
    id = 'idAsignatura'


class Practica_laboralViewSet(GenericViewSet):
    queryset = Practica_laboral.objects.all()
    serializer_class = Practica_laboralSerializer
    model = Practica_laboral
    id = 'idAsignatura'


# class BibliografiaViewSet(GenericViewSet):
#     queryset = Bibliografia.objects.all()
#     serializer_class = BibliografiaSerializer
#     model = Bibliografia
#     id = 'idBibliografia'


# class SoftwareViewSet(GenericViewSet):
#     queryset = Software.objects.all()
#     serializer_class = SoftwareSerializer
#     model = Software
#     id = 'idSoftware'


class Alumno_ayudanteViewSet(GenericViewSet):
    queryset = Alumno_ayudante.objects.all()
    serializer_class = Alumno_ayudanteSerializer
    model = Alumno_ayudante
    id = 'idAlumno_ayudante'


class DisciplinaViewSet(GenericViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    model = Disciplina
    id = 'idDisciplina'


class AsignaturaViewSet(GenericViewSet):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer
    model = Asignatura
    id = 'idAsignatura'


class Asignatura_ejIntegradorViewSet(GenericViewSet):
    queryset = Asignatura_ejIntegrador.objects.all()
    serializer_class = Asignatura_ejIntegradorSerializer
    model = Asignatura_ejIntegrador
    id = 'idAsignatura_ejIntegrador'


class Trabajo_diplomaViewSet(GenericViewSet):
    queryset = Trabajo_diploma.objects.all()
    serializer_class = Trabajo_diplomaSerializer
    model = Trabajo_diploma
    id = 'idTrabajo_diploma'


class DepartamentoViewSet(GenericViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    model = Departamento
    id = 'idDepartamento'


class EstudianteViewSet(GenericViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    model = Estudiante
    id = 'idEstudiante'


class Trab_diploma_profesor_estudianteViewSet(GenericViewSet):
    queryset = Trab_diploma_profesor_estudiante.objects.all()
    serializer_class = Trab_diploma_profesor_estudianteSerializer
    model = Trab_diploma_profesor_estudiante
    id = 'idTrab_diploma_profesor_estudiante'


class ProyectoViewSet(GenericViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
    model = Proyecto
    id = 'idProyecto'


class InvestigacionViewSet(GenericViewSet):
    queryset = Investigacion.objects.all()
    serializer_class = InvestigacionSerializer
    model = Investigacion
    id = 'idProyecto'


class ExtensionistaViewSet(GenericViewSet):
    queryset = Extensionista.objects.all()
    serializer_class = ExtensionistaSerializer
    model = Extensionista
    id = 'idProyecto'


# ===================================================================================================================================================#

class ComunitarioViewSet(GenericViewSet):
    queryset = Comunitario.objects.all()
    serializer_class = ComunitarioSerializer
    model = Comunitario
    id = 'idProyecto'


# ===================================================================================================================================================#


class Catedra_honorificaViewSet(GenericViewSet):
    queryset = Catedra_honorifica.objects.all()
    serializer_class = Catedra_honorificaSerializer
    model = Catedra_honorifica
    id = 'idProyecto'


# ===================================================================================================================================================#

class Ejercicio_integradorViewSet(GenericViewSet):
    queryset = Ejercicio_integrador.objects.all()
    serializer_class = Ejercicio_integradorSerializer
    model = Ejercicio_integrador
    id = 'idEjercicio_integrador'


class Asignatura_profesorViewSet(GenericViewSet):
    queryset = Asignatura_profesor.objects.all()
    serializer_class = Asignatura_profesorSerializer
    model = Asignatura_profesor
    id = 'idAsignatura_profesor'

class PublicacionViewSet(GenericViewSet):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer
    model = Publicacion
    id = 'idPublicacion'

class LibroViewSet(GenericViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    model = Libro
    id = 'idPublicacion'

class RevistaViewSet(GenericViewSet):
    queryset = Revista.objects.all()
    serializer_class = RevistaSerializer
    model = Revista
    id = 'idPublicacion'

class TrabajadorViewSet(GenericViewSet):
    queryset = Trabajador.objects.all()
    serializer_class = TrabajadorSerializer
    model = Trabajador
    id = 'idTrabajador'

class ProfesorViewSet(GenericViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    model = Profesor
    id = 'idTrabajador'

class Profesor_disciplinaViewSet(GenericViewSet):
    queryset = Profesor_disciplina.objects.all()
    serializer_class = Profesor_disciplinaSerializer
    model = Profesor_disciplina
    id = 'idProfesor_disciplina'

class Cargo_metodologicoViewSet(GenericViewSet):
    queryset = Cargo_metodologico.objects.all()
    serializer_class = Cargo_metodologicoSerializer
    model = Cargo_metodologico
    id = 'idCargo_metodologico'

class Profesor_cargo_metodologicoViewSet(GenericViewSet):
    queryset = Profesor_cargo_metodologico.objects.all()
    serializer_class = Profesor_cargo_metodologicoSerializer
    model = Profesor_cargo_metodologico
    id = 'idProfesor_cargo_metodologico'

class Profesor_posgradoViewSet(GenericViewSet):
    queryset = Profesor_posgrado.objects.all()
    serializer_class = Profesor_posgradoSerializer
    model = Profesor_posgrado
    id = 'idProfesor_posgrado'

class Trabajador_no_docenteViewSet(GenericViewSet):
    queryset = Trabajador_no_docente.objects.all()
    serializer_class = Trabajador_no_docenteSerializer
    model = Trabajador_no_docente
    id = 'idTrabajador'


class PremioViewSet(GenericViewSet):
    queryset = Premio.objects.all()
    serializer_class = PremioSerializer
    model = Premio
    id = 'idPremio'

class Ponencia_eventoViewSet(GenericViewSet):
    queryset = Ponencia_evento.objects.all()
    serializer_class = Ponencia_eventoSerializer
    model = Ponencia_evento
    id = 'idEvento'


# =====================================================================START TABLES LIETIS===========================================================#


class Estudiante_posgradoViewSet(GenericViewSet):
    queryset = Estudiante_posgrado.objects.all()
    serializer_class = Estudiante_posgradoSerializer
    model = Estudiante_posgrado
    id = 'idEstudiante_posgrado'
# ===================================================================================================================================================#


class PosgradoViewSet(GenericViewSet):
    queryset = Posgrado.objects.all()
    serializer_class = PosgradoSerializer
    model = Posgrado
    id = 'idPosgrado'

class ExpedientesSinPosgradoView(APIView):
    def get(self, request):
        expedientes = Expediente.objects.filter(posgrado=None)
        serializer = ExpedienteSerializer(expedientes, many=True)
        return Response(serializer.data)
    
# ===================================================================================================================================================#


class ExpedienteViewSet(GenericViewSet):
    queryset = Expediente.objects.all()
    serializer_class = ExpedienteSerializer
    model = Expediente
    id = 'idExpediente'
