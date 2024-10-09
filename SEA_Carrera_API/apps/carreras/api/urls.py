from rest_framework import routers
from django.urls import path
from .viewsets.carrera import *

router = routers.SimpleRouter()

urlpatterns = router.urls 

router.register('laboratorio',LaboratorioViewSet)
router.register('estudiante',EstudianteViewSet)
router.register('carrera',CarreraViewSet)
router.register('departamento',DepartamentoViewSet)
router.register('datos_promocion',Datos_promocionViewSet)
router.register('egresado',EgresadoViewSet)
router.register('asignatura_virtual',Asignatura_virtualViewSet)
router.register('practica_laboral',Practica_laboralViewSet)
# router.register('bibliografia',BibliografiaViewSet)
# router.register('software',SoftwareViewSet)
router.register('alumno_ayudante',Alumno_ayudanteViewSet)




router.register('disciplina',DisciplinaViewSet)
router.register('asignatura',AsignaturaViewSet)
router.register('ejercicio_integrador_asignatura',Asignatura_ejIntegradorViewSet)
router.register('trabajo_diploma',Trabajo_diplomaViewSet)
router.register('trab_diploma_profesor_estudiante',Trab_diploma_profesor_estudianteViewSet)
router.register('proyecto',ProyectoViewSet)
router.register('investigacion',InvestigacionViewSet)
router.register('extensionista',ExtensionistaViewSet)
router.register('comunitario',ComunitarioViewSet)
router.register('catedra_honorifica',Catedra_honorificaViewSet)
router.register('ejercicio_integrador',Ejercicio_integradorViewSet)
router.register('asignatura_profesor',Asignatura_profesorViewSet)

# # ------------------------------------------START TABLES HECTOR------------------------------------------------------------

router.register('publicacion',PublicacionViewSet)
router.register('libro',LibroViewSet)
router.register('revista',RevistaViewSet)
router.register('trabajador',TrabajadorViewSet)
router.register('profesor',ProfesorViewSet)
router.register('profesor_cargo_metodologico',Profesor_cargo_metodologicoViewSet)
router.register('profesor_posgrado',Profesor_posgradoViewSet)
router.register('cargo_metodologico',Cargo_metodologicoViewSet)
router.register('profesor_disciplina',Profesor_disciplinaViewSet)
router.register('trabajador_no_docente',Trabajador_no_docenteViewSet)
router.register('premio',PremioViewSet)
# # ------------------------------------------END TABLES HECTOR------------------------------------------------------------
# # ------------------------------------------START TABLES LIETIS------------------------------------------------------------
router.register('evento',Ponencia_eventoViewSet)
router.register('estudiante_posgrado',Estudiante_posgradoViewSet )
router.register('posgrado',PosgradoViewSet)
router.register('expediente',ExpedienteViewSet)
# ------------------------------------------END TABLES LIETIS------------------------------------------------------------



urlpatterns = [
    path('expedientes_sin_posgrado/', ExpedientesSinPosgradoView.as_view(), name='expedientes_sin_posgrado'),
] + router.urls



