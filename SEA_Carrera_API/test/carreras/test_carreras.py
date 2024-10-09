from test.test_setup import TestSetUp
from rest_framework import status
from faker import Faker
from test.carreras.faker_db import SEACarrera_faker_JSON
from apps.carreras.api.viewsets import *


class TestCase(TestSetUp):

    faker = Faker()
   
#    -----------------------------------------BEGIN BIBLIOGRAFÍAS----------------------------------------------------------
    def test_create_bibliografia(self):
        bibliografia = SEACarrera_faker_JSON().build_bibliografia()

        url = '/gestion/bibliografia/'
        response = self.client.post(url, bibliografia, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return response.data['idBibliografia']

    def test_update_bibliografia(self):
        idBibliografia = self.test_create_bibliografia()
        bibliografia = SEACarrera_faker_JSON().build_bibliografia()
        url = '/gestion/bibliografia/'
        response = self.client.put(url+str(idBibliografia)+'/', bibliografia, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_bibliografia(self):
        response = self.client.get("/gestion/bibliografia/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_bibliografia(self):
        idBibliografia = self.test_create_bibliografia()
        response = self.client.get("/gestion/bibliografia/"+str(idBibliografia)+'/', format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_bibliografia(self):
        idBibliografia = self.test_create_bibliografia()
        response = self.client.delete("/gestion/bibliografia/"+str(idBibliografia)+'/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#    -----------------------------------------END BIBLIOGRAFÍAS----------------------------------------------------------
#    -----------------------------------------BEGIN SOFTWARES----------------------------------------------------------
    def test_create_software(self):
        software = SEACarrera_faker_JSON().build_software()

        url = '/gestion/software/'
        response = self.client.post(url, software, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.idSoftware = response.data['idSoftware']
        return self.idSoftware

    def test_update_software(self):
        idSoftware = self.test_create_software()
        software = SEACarrera_faker_JSON().build_software()
        url = '/gestion/software/'
        response = self.client.put(url+str(idSoftware)+'/', software, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_software(self):
        response = self.client.get("/gestion/software/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_software(self):
        idSoftware = self.test_create_software()
        response = self.client.get("/gestion/software/"+str(idSoftware)+'/', format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_software(self):
        idSoftware = self.test_create_software()
        response = self.client.delete("/gestion/software/"+str(idSoftware)+'/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#    -----------------------------------------END SOFTWARES----------------------------------------------------------

#    -----------------------------------------BEGIN DEPARTAMENTOS----------------------------------------------------------
    def test_create_departamento(self):
        departamento = SEACarrera_faker_JSON().build_departamento()
        url = '/gestion/departamento/'
        response = self.client.post(url, departamento, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.idDepartamento = response.data['idDepartamento']
        return self.idDepartamento

    def test_update_departamento(self):
        idDepartamento = self.test_create_departamento()
        departamento = SEACarrera_faker_JSON().build_departamento()
        url = '/gestion/departamento/'
        response = self.client.put(url+str(idDepartamento)+'/', departamento, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_departamento(self):
        response = self.client.get("/gestion/departamento/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_departamento(self):
        idDepartamento = self.test_create_departamento()
        response = self.client.get("/gestion/departamento/"+str(idDepartamento)+'/', format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_departamento(self):
        idDepartamento = self.test_create_departamento()
        response = self.client.delete("/gestion/departamento/"+str(idDepartamento)+'/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#    -----------------------------------------END DEPARTAMENTOS----------------------------------------------------------
#    -----------------------------------------BEGIN CARRERAS----------------------------------------------------------
    def test_create_carrera(self):
        # Arrange
        url = '/gestion/carrera/'
        idDepartamento = self.test_create_departamento()
        carrera = {
            "idCarrera": self.faker.random_number(digits=3),
            "nombre_carrera": "Ingeniería informática ",
            "agno_academico": "5",
            "plan_estudio": "E",
            # "modalidad": "diurno",
            "unidades_docente":"ATI",
            "idDepartamento": idDepartamento      
        }
        # Act
        response = self.client.post(url, carrera, format='json')
        # Assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.idCarrera = response.data['idCarrera']
        return self.idCarrera
    
    def test_update_carrera(self):
        idCarrera = self.test_create_carrera()
        idDepartamento = self.test_create_departamento()
        carrera = {
            "nombre_carrera": self.faker.name(),
            "agno_academico": '1',
            "plan_estudio": self.faker.word(),
            "modalidad": self.faker.word(),
            "unidades_docente":self.faker.word(),
            "idDepartamento": idDepartamento      
        }

        url = '/gestion/carrera/'
        response = self.client.put(url+str(idCarrera)+'/', carrera, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_carrera(self):
        response = self.client.get("/gestion/carrera/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_carrera(self):
        idCarrera = self.test_create_carrera()
        response = self.client.get("/gestion/carrera/"+str(idCarrera)+'/', format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_carrera(self):
        idCarrera = self.test_create_carrera()
        response = self.client.delete("/gestion/carrera/"+str(idCarrera)+'/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#    -----------------------------------------END CARRERAS----------------------------------------------------------

#    -----------------------------------------BEGIN DISCIPLINAS----------------------------------------------------------
    def test_create_disciplina(self):
        idCarrera = self.test_create_carrera()
        disciplina = {
            'idDisciplina': self.faker.random_number(digits=3),
            'nombre_disciplina': self.faker.word(),
            "profesor": self.faker.name(),
            "jefe": self.faker.name(),
            "idCarrera": idCarrera
        }

        url = '/gestion/disciplina/'
        response = self.client.post(url, disciplina, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.idDisciplina = response.data['idDisciplina']
        return self.idDisciplina

    def test_update_disciplina(self):
        idCarrera = self.test_create_carrera()
        idDisciplina = self.test_create_disciplina()
        disciplina = {
            'nombre_disciplina': self.faker.word(),
            "profesor": self.faker.name(),
            "jefe": self.faker.name(),
            "idCarrera": idCarrera
        }
        url = '/gestion/disciplina/'
        response = self.client.put(url+str(idDisciplina)+'/', disciplina, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_disciplina(self):
        response = self.client.get("/gestion/disciplina/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_disciplina(self):
        idDisciplina = self.test_create_disciplina()
        response = self.client.get("/gestion/disciplina/"+str(idDisciplina)+'/', format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_disciplina(self):
        idDisciplina = self.test_create_disciplina()      
        response = self.client.delete("/gestion/disciplina/"+str(idDisciplina)+'/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#    -----------------------------------------END DISCIPLINAS----------------------------------------------------------

#    -----------------------------------------BEGIN TRABAJOS DE DIPLOMA----------------------------------------------------------
    def test_create_trabajo_diploma(self):
        trabajo_diploma = SEACarrera_faker_JSON().build_trabajo_diploma()

        url = '/gestion/trabajo_diploma/'
        response = self.client.post(url, trabajo_diploma, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.idTrabajo_diploma = response.data['idTrabajo_diploma']
        return self.idTrabajo_diploma

    def test_update_trabajo_diploma(self):
        idTrabajo_diploma = self.test_create_trabajo_diploma()
        trabajo_diploma = SEACarrera_faker_JSON().build_trabajo_diploma()
        url = '/gestion/trabajo_diploma/'
        response = self.client.put(url+str(idTrabajo_diploma)+'/', trabajo_diploma, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_trabajo_diploma(self):
        response = self.client.get("/gestion/trabajo_diploma/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_trabajo_diploma(self):
        idTrabajo_diploma = self.test_create_trabajo_diploma()
        response = self.client.get("/gestion/trabajo_diploma/"+str(idTrabajo_diploma)+'/', format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_trabajo_diploma(self):
        idTrabajo_diploma = self.test_create_trabajo_diploma()
        response = self.client.delete("/gestion/trabajo_diploma/"+str(idTrabajo_diploma)+'/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#    -----------------------------------------END TRABAJOS DE DIPLOMA----------------------------------------------------------

#    -----------------------------------------BEGIN EXPEDIENTE----------------------------------------------------------
    def create_expediente(self):
        expediente = {
            'idExpediente': self.faker.random_number(digits=3),
            # 'archivos': 'documents/'
        }

        url = '/gestion/expediente/'
        response = self.client.post(url, expediente, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return  response.data['idExpediente']

#    -----------------------------------------END EXPEDIENTE----------------------------------------------------------
#    -----------------------------------------BEGIN POSGRADO----------------------------------------------------------
    def create_posgrado(self):
        idExpediente = self.create_expediente()
        posgrado = {
            'idPosgrado': self.faker.random_number(digits=3),
            'nombre': self.faker.name(),
            'fecha': '2022-11-12',
            'edicion': self.faker.word(),
            'programa': self.faker.word(),
            'fecha_culminacion': '2022-11-12',
            'reconocimiento': 'M',
            'matricula_inicial': self.faker.random_number(digits=2),
            'matricula_final': self.faker.random_number(digits=2),
            'convenio': self.faker.word(),
            'categoria_cientifica': self.faker.word(),
            'tipo_posgrado': self.faker.word(),
            'encuesta_satisfaccion': self.faker.word(),
            'idExpediente': idExpediente,
        }

        url = '/gestion/posgrado/'
        response = self.client.post(url, posgrado, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return  response.data['idPosgrado']

#    -----------------------------------------END POSGRADO----------------------------------------------------------
#    -----------------------------------------BEGIN TRABAJADOR DOCENTE----------------------------------------------------------
    def create_trabajador_docente(self):
        idPosgrado = self.create_posgrado()
        idTrabajo_diploma = self.test_create_trabajo_diploma()

        trabajador_docente = {
            'idTrabajador': self.faker.random_number(digits=3),
            'nombre': self.faker.name(),
            'apellido': self.faker.word(),
            'carnet_identidad': str(self.faker.random_number(digits=11)),
            'edad': self.faker.random_number(digits=2),
            'sexo': 'M',
            'direccion': "una direccion",
            'telefono': str(self.faker.random_number(digits=8)),
            'titulo_academico': self.faker.word(),
            'fecha_graduacion': '2022-11-12',
            'agno_inicial_trabajador': self.faker.random_number(digits=2),
            'trabajador_departamento': True,
            'militancia': True,
            'cargo_direccion': self.faker.word(),
            'cargo_metodologico': self.faker.word(),
            'doctor': 'M',
            'categoria_docente': "una direccion",
            'agnos_exp_educ_superior': self.faker.random_number(digits=2),
            'tutor': True,
            'otras_funciones': self.faker.word(),
            'jefe_departamento': 'si',
            'idPosgrado': idPosgrado,
            'idTrabajo_diploma': [idTrabajo_diploma],
        }

        url = '/gestion/trabajador_docente/'
        response = self.client.post(url, trabajador_docente, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return  response.data['idTrabajador']

#    -----------------------------------------END TRABAJADOR----------------------------------------------------------
#    -----------------------------------------BEGIN ASIGNATURAS----------------------------------------------------------
    def test_create_asignatura(self):
        idDisciplina = self.test_create_disciplina()
        idTrabajador = self.create_trabajador_docente()
        idBibliografia = self.test_create_bibliografia()
        idSoftware = self.test_create_software()
        asignatura = {
            'idAsignatura': self.faker.random_number(digits=3),
            'nombre_asignatura': self.faker.word(),
            'cant_horas': self.faker.random_number(digits=3),
            'horas_totales': self.faker.random_number(digits=3),
            'tipo_curriculum': self.faker.word(),
            'tipo_evaluacion_final': self.faker.word(),
            'virtual': "No",
            'agno':'5',
            'objetivo': self.faker.word(),
            'idDisciplina': idDisciplina,
            'idTrabajador': idTrabajador,
            'idBibliografia': [idBibliografia],
            'idSoftware': [idSoftware]
        }
        url = '/gestion/asignatura/'
        response = self.client.post(url, asignatura, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.idAsignatura = response.data['idAsignatura']
        return self.idAsignatura

    def test_update_asignatura(self):
        idAsignatura = self.test_create_asignatura()
        idDisciplina = self.test_create_disciplina()
        idTrabajador = self.create_trabajador_docente()
        idBibliografia = self.test_create_bibliografia()
        idSoftware = self.test_create_software()
        asignatura = {
            'nombre_asignatura': self.faker.word(),
            'cant_horas': self.faker.random_number(digits=3),
            'horas_totales': self.faker.random_number(digits=3),
            'tipo_curriculum': self.faker.word(),
            'tipo_evaluacion_final': self.faker.word(),
            'virtual': "No",
            'agno': '5',
            'objetivo': self.faker.word(),
            'idDisciplina': idDisciplina,
            'idTrabajador': idTrabajador,
            'idBibliografia': [idBibliografia],
            'idSoftware': [idSoftware]
        }
        url = '/gestion/asignatura/'
        response = self.client.put(url+str(idAsignatura)+'/', asignatura, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_asignatura(self):
        response = self.client.get("/gestion/asignatura/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_asignatura(self):
        idAsignatura = self.test_create_asignatura() 
        response = self.client.get("/gestion/asignatura/"+str(idAsignatura)+'/', format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_asignatura(self):
        idAsignatura = self.test_create_asignatura() 
        response = self.client.delete("/gestion/asignatura/"+str(idAsignatura)+'/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#    -----------------------------------------END ASIGNATURAS----------------------------------------------------------
#    -----------------------------------------BEGIN PRÁCTICAS LABORALES----------------------------------------------------------
    def test_create_practica_laboral(self):
        idDisciplina = self.test_create_disciplina()
        idTrabajador = self.create_trabajador_docente()
        idBibliografia = self.test_create_bibliografia()
        idSoftware = self.test_create_software()
        practica_laboral = {
            'idAsignatura': self.faker.random_number(digits=3),
            'nombre_asignatura': self.faker.word(),
            'cant_horas': self.faker.random_number(),
            'horas_totales': self.faker.random_number(),
            'tipo_curriculum': self.faker.word(),
            'tipo_evaluacion_final': self.faker.word(),
            'virtual': "No",
            'agno': '3',
            'objetivo': self.faker.word(),
            'idDisciplina': idDisciplina,
            'idTrabajador': idTrabajador,
            'idBibliografia': [idBibliografia],
            'idSoftware': [idSoftware],
            'tema_practica_laboral': self.faker.word(),
            'lugar_ubicacion': self.faker.word(),
            "nota": '4',
        }

        url = '/gestion/practica_laboral/'
        response = self.client.post(url, practica_laboral, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return response.data['idAsignatura']

    def test_update_practica_laboral(self):
        idAsignatura = self.test_create_practica_laboral()
        idDisciplina = self.test_create_disciplina()
        idTrabajador = self.create_trabajador_docente()
        idBibliografia = self.test_create_bibliografia()
        idSoftware = self.test_create_software()

        practica_laboral = {
            'nombre_asignatura': self.faker.word(),
            'cant_horas': self.faker.random_number(),
            'horas_totales': self.faker.random_number(),
            'tipo_curriculum': self.faker.word(),
            'tipo_evaluacion_final': self.faker.word(),
            'virtual': "No",
            'agno': '2',
            'objetivo': self.faker.word(),
            'idDisciplina': idDisciplina,
            'idTrabajador': idTrabajador,
            'idBibliografia': [idBibliografia],
            'idSoftware': [idSoftware],
            'tema_practica_laboral': self.faker.word(),
            'lugar_ubicacion': self.faker.word(),
            "nota": '3',
        }

        url = '/gestion/practica_laboral/'
        response = self.client.put(url+str(idAsignatura)+'/', practica_laboral, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_practica_laboral(self):
        response = self.client.get("/gestion/practica_laboral/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_practica_laboral(self):
        idAsignatura = self.test_create_practica_laboral()
        response = self.client.get("/gestion/practica_laboral/"+str(idAsignatura)+'/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_practica_laboral(self):
        idAsignatura = self.test_create_practica_laboral()
        response = self.client.delete("/gestion/practica_laboral/"+str(idAsignatura)+'/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#    -----------------------------------------END PRÁCTICAS LABORALES----------------------------------------------------------
#    -----------------------------------------BEGIN PREGRADO----------------------------------------------------------
    def test_create_pregrado(self):
        idDisciplina = self.test_create_disciplina()
        idTrabajador = self.create_trabajador_docente()
        idBibliografia = self.test_create_bibliografia()
        idSoftware = self.test_create_software()
        pregrado = {
            'idAsignatura': self.faker.random_number(digits=3),
            'nombre_asignatura': self.faker.word(),
            'cant_horas': self.faker.random_number(),
            'horas_totales': self.faker.random_number(),
            'tipo_curriculum': self.faker.word(),
            'tipo_evaluacion_final': self.faker.word(),
            'virtual': "No",
            'agno': '3',
            'objetivo': self.faker.word(),
            'idDisciplina': idDisciplina,
            'idTrabajador': idTrabajador,
            'idBibliografia': [idBibliografia],
            'idSoftware': [idSoftware],
            "alumnoAyudante": "Si"
        }

        url = '/gestion/pregrado/'
        response = self.client.post(url, pregrado, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return response.data['idAsignatura']

    def test_update_pregrado(self):
        idAsignatura = self.test_create_pregrado()
        idDisciplina = self.test_create_disciplina()
        idTrabajador = self.create_trabajador_docente()
        idBibliografia = self.test_create_bibliografia()
        idSoftware = self.test_create_software()
        pregrado = {
            'idAsignatura': self.faker.random_number(digits=3),
            'nombre_asignatura': self.faker.word(),
            'cant_horas': self.faker.random_number(),
            'horas_totales': self.faker.random_number(),
            'tipo_curriculum': self.faker.word(),
            'tipo_evaluacion_final': self.faker.word(),
            'virtual': "No",
            'agno': '4',
            'objetivo': self.faker.word(),
            'idDisciplina': idDisciplina,
            'idTrabajador': idTrabajador,
            'idBibliografia': [idBibliografia],
            'idSoftware': [idSoftware],
            "alumnoAyudante": "Si"
        }
        url = '/gestion/pregrado/'
        response = self.client.put(url+str(idAsignatura)+'/', pregrado, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_pregrado(self):
        response = self.client.get("/gestion/pregrado/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_pregrado(self):
        idAsignatura = self.test_create_pregrado()
        response = self.client.get("/gestion/pregrado/"+str(idAsignatura)+'/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_pregrado(self):
        idAsignatura = self.test_create_pregrado()
        response = self.client.delete("/gestion/pregrado/"+str(idAsignatura)+'/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#    -----------------------------------------END PREGRADO----------------------------------------------------------
#    -----------------------------------------BEGIN ALUMNOS AYUDANTES----------------------------------------------------------
    def test_create_alumno_ayudante(self):
        idAsignatura = self.test_create_pregrado()
        alumno_ayudante = {
            'idAlumno_ayudante': self.faker.random_number(digits=3),
            'nombre_alumno_ayudante': self.faker.name(),
            'apellido': self.faker.name(),
            'agno_academico': '4',
            # 'plan':  "hvFvRfzQREXAY_bHkq6dL",
            "idAsignatura": idAsignatura
        }

        url = '/gestion/alumno_ayudante/'
        response = self.client.post(url, alumno_ayudante, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return response.data['idAlumno_ayudante']

    def test_update_alumno_ayudante(self):
        idAlumno_ayudante = self.test_create_alumno_ayudante()
        idAsignatura = self.test_create_pregrado()
        alumno_ayudante = {
            'idAlumno_ayudante': self.faker.random_number(digits=3),
            'nombre_alumno_ayudante': self.faker.name(),
            'apellido': self.faker.name(),
            'agno_academico': '2',
            # 'plan': "plan",
            "idAsignatura": idAsignatura
        }
        url = '/gestion/alumno_ayudante/'
        response = self.client.put(url+str(idAlumno_ayudante)+'/', alumno_ayudante, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_alumno_ayudante(self):
        response = self.client.get("/gestion/alumno_ayudante/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_alumno_ayudante(self):
        idAlumno_ayudante = self.test_create_alumno_ayudante()
        response = self.client.get("/gestion/alumno_ayudante/"+str(idAlumno_ayudante)+'/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_alumno_ayudante(self):
        idAlumno_ayudante = self.test_create_alumno_ayudante()
        response = self.client.delete("/gestion/alumno_ayudante/"+str(idAlumno_ayudante)+'/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#    -----------------------------------------END ALUMNOS AYUDANTES----------------------------------------------------------
#    -----------------------------------------BEGIN ESTUDIANTES----------------------------------------------------------
    def test_create_estudiante(self):
        idTrabajo_diploma = self.test_create_trabajo_diploma()
        estudiante = {
            'idEstudiante': self.faker.random_number(digits=3),
            'nombre_estudiante': self.faker.name(),
            "apellido": self.faker.name(),
            "carnet_identidad": '2316518946',
            "año_academico": '5',
            "disponibilidad_tecnologica": 'Si',
            "idTrabajo_diploma": idTrabajo_diploma,
        }
        url = '/gestion/estudiante/'
        response = self.client.post(url, estudiante, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.idEstudiante = response.data['idEstudiante']
        return self.idEstudiante

    def test_update_estudiante(self):
        idEstudiante = self.test_create_estudiante()
        idTrabajo_diploma = self.test_create_trabajo_diploma()
        estudiante = {
           'idEstudiante': self.faker.random_number(digits=3),
            'nombre_estudiante': self.faker.name(),
            "apellido": self.faker.name(),
            "carnet_identidad": '65498465',
            "año_academico": '4',
            "disponibilidad_tecnologica": 'Si',
            "idTrabajo_diploma": idTrabajo_diploma,
        }
        url = '/gestion/estudiante/'
        response = self.client.put(url+str(idEstudiante)+'/', estudiante, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_estudiante(self):
        response = self.client.get("/gestion/estudiante/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_estudiante(self):
        idEstudiante = self.test_create_estudiante()
        response = self.client.get("/gestion/estudiante/"+str(idEstudiante)+'/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_estudiante(self):
        idEstudiante = self.test_create_estudiante()
        response = self.client.delete("/gestion/estudiante/"+str(idEstudiante)+'/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#    -----------------------------------------END ESTUDIANTES----------------------------------------------------------
#    -----------------------------------------BEGIN ASIGNATURA - ESTUDIANTES----------------------------------------------------------
    def test_create_asignatura_estudiante(self):
        idEstudiante = self.test_create_estudiante()
        idAsignatura = self.test_create_asignatura()
        asignatura_estudiante = {
            'idAsignatura_estudiante': self.faker.random_number(digits=3),
            'idEstudiante': idEstudiante,
            "idAsignatura": idAsignatura,
            "nota": '3'
        }
        url = '/gestion/asignatura_estudiante/'
        response = self.client.post(url, asignatura_estudiante, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return response.data['idAsignatura_estudiante']

    def test_update_asignatura_estudiante(self):
        idAsignatura_estudiante = self.test_create_asignatura_estudiante()
        idEstudiante = self.test_create_estudiante()
        idAsignatura = self.test_create_asignatura()
        asignatura_estudiante = {
            'idAsignatura_estudiante': self.faker.random_number(digits=3),
            'idEstudiante': idEstudiante,
            "idAsignatura": idAsignatura,
            "nota": '2'
        }
        url = '/gestion/asignatura_estudiante/'
        response = self.client.put(url+str(idAsignatura_estudiante)+'/', asignatura_estudiante, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_asignatura_estudiante(self):
        response = self.client.get("/gestion/asignatura_estudiante/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_asignatura_estudiante(self):
        idAsignatura_estudiante = self.test_create_asignatura_estudiante()
        response = self.client.get("/gestion/asignatura_estudiante/"+str(idAsignatura_estudiante)+'/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_asignatura_estudiante(self):
        idAsignatura_estudiante = self.test_create_asignatura_estudiante()
        response = self.client.delete("/gestion/asignatura_estudiante/"+str(idAsignatura_estudiante)+'/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#    -----------------------------------------END ESTUDIANTES----------------------------------------------------------

#    -----------------------------------------BEGIN LABORATORIOS----------------------------------------------------------
    def test_create_laboratorio(self):
        idCarrera = self.test_create_carrera()
        laboratorio = {
            'idLaboratorio': self.faker.random_number(digits=3),
            'numero': self.faker.random_number(digits=3),
            'responsable': self.faker.word(),
            'equipamento': self.faker.word(),
            'idCarrera': idCarrera
        }
        url = '/gestion/laboratorio/'
        response = self.client.post(url, laboratorio, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return response.data['idLaboratorio']

    def test_update_laboratorio(self):
        idCarrera = self.test_create_carrera()
        idLaboratorio = self.test_create_laboratorio()
        laboratorio = {
            'idLaboratorio': self.faker.random_number(digits=3),
            'numero': self.faker.random_number(digits=3),
            'responsable': self.faker.word(),
            'equipamento': self.faker.word(),
            'idCarrera': idCarrera
        }
        url = '/gestion/laboratorio/'
        response = self.client.put(url+str(idLaboratorio)+'/', laboratorio, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_laboratorio(self):
        response = self.client.get("/gestion/laboratorio/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_laboratorio(self):
        idLaboratorio = self.test_create_laboratorio()
        response = self.client.get("/gestion/laboratorio/"+str(idLaboratorio)+'/', format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_laboratorio(self):
        idLaboratorio = self.test_create_laboratorio()
        response = self.client.delete("/gestion/laboratorio/"+str(idLaboratorio)+'/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#    -----------------------------------------END LABORATORIOS----------------------------------------------------------

#    -----------------------------------------BEGIN PROYECTOS----------------------------------------------------------
    def test_create_proyecto(self):
        idEstudiante = self.test_create_estudiante()
        proyecto = {
            'idProyecto': self.faker.random_number(digits=3),
            'nombre_proyecto': self.faker.word(),
            "agno_experiencia": self.faker.random_number(digits=2),
            "lider_proyecto": self.faker.name(),
            "idEstudiante": [idEstudiante],
        }

        url = '/gestion/proyecto/'
        response = self.client.post(url, proyecto, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.idProyecto = response.data['idProyecto']
        return self.idProyecto

    def test_update_proyecto(self):
        # print('t_update_departamento')
        idProyecto = self.test_create_proyecto()
        idEstudiante = self.test_create_estudiante()
        proyecto = {
            'nombre_proyecto': self.faker.word(),
            "agno_experiencia": self.faker.random_number(digits=3),
            "lider_proyecto": self.faker.name(),
            "idEstudiante": [idEstudiante],
        }
        url = '/gestion/proyecto/'
        response = self.client.put(url+str(idProyecto)+'/', proyecto, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_proyecto(self):
        response = self.client.get("/gestion/proyecto/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_proyecto(self):
        idProyecto = self.test_create_proyecto()
        response = self.client.get("/gestion/proyecto/"+str(idProyecto)+'/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_proyecto(self):
        idProyecto = self.test_create_proyecto()
        response = self.client.delete("/gestion/proyecto/"+str(idProyecto)+'/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#    -----------------------------------------END PROYECTOS----------------------------------------------------------
#    -----------------------------------------BEGIN PROYECTOS DE INVESTIGACIÓN----------------------------------------------------------
    def test_create_investigacion(self):
        idEstudiante = self.test_create_estudiante()
        investigacion = {
            'idProyecto': self.faker.random_number(digits=3),
            'nombre_proyecto': self.faker.word(),
            "agno_experiencia": self.faker.random_number(digits=3),
            "lider_proyecto": self.faker.name(),
            "idEstudiante": [idEstudiante],
            "clasificacion": self.faker.word()
        }

        url = '/gestion/investigacion/'
        response = self.client.post(url, investigacion, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.idProyecto = response.data['idProyecto']
        return self.idProyecto

    def test_update_investigacion(self):
        idProyecto = self.test_create_investigacion()
        idEstudiante = self.test_create_estudiante()
        investigacion = {
            'nombre_proyecto': self.faker.word(),
            "agno_experiencia": self.faker.random_number(digits=3),
            "lider_proyecto": self.faker.name(),
            "idEstudiante": [idEstudiante],
             "clasificacion": self.faker.word()
        }
        url = '/gestion/investigacion/'
        response = self.client.put(url+str(idProyecto)+'/', investigacion, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_investigacion(self):
        response = self.client.get("/gestion/investigacion/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_investigacion(self):
        idProyecto = self.test_create_investigacion()
        response = self.client.get("/gestion/investigacion/"+str(idProyecto)+'/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_investigacion(self):
        idProyecto = self.test_create_investigacion()
        response = self.client.delete("/gestion/investigacion/"+str(idProyecto)+'/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#    -----------------------------------------END PROYECTOS DE INVESTIGACIÓN----------------------------------------------------------
#    -----------------------------------------BEGIN PROYECTOS EXTENSIONISTAS----------------------------------------------------------
    def test_create_extensionista(self):
        idEstudiante = self.test_create_estudiante()
        extensionista = {
            'idProyecto': self.faker.random_number(digits=3),
            'nombre_proyecto': self.faker.word(),
            "agno_experiencia": self.faker.random_number(digits=3),
            "lider_proyecto": self.faker.name(),
            "idEstudiante": [idEstudiante],
            # "tareas_impacto": "tareas_impacto",
            # "tareas_extensionista": "tareas_extensionista",
        }

        url = '/gestion/extensionista/'
        response = self.client.post(url, extensionista, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.idProyecto = response.data['idProyecto']
        return self.idProyecto

    def test_update_extensionista(self):
        idProyecto = self.test_create_extensionista()
        idEstudiante = self.test_create_estudiante()
        extensionista = {
            'idProyecto': self.faker.random_number(digits=3),
            'nombre_proyecto': self.faker.word(),
            "agno_experiencia": self.faker.random_number(digits=3),
            "lider_proyecto": self.faker.name(),
            "idEstudiante": [idEstudiante],
            # "tareas_impacto": "tareas_impacto",
            # "tareas_extensionista": "tareas_extensionista",
        }
        url = '/gestion/extensionista/'
        response = self.client.put(url+str(idProyecto)+'/', extensionista, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_extensionista(self):
        response = self.client.get("/gestion/extensionista/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_extensionista(self):
        idProyecto = self.test_create_extensionista()
        response = self.client.get("/gestion/extensionista/"+str(idProyecto)+'/', format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_extensionista(self):
        idProyecto = self.test_create_extensionista()
        response = self.client.delete("/gestion/extensionista/"+str(idProyecto)+'/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#    -----------------------------------------END PROYECTOS EXTENSIONISTAS----------------------------------------------------------
#    -----------------------------------------BEGIN PROYECTOS COMUNITARIOS----------------------------------------------------------
    def test_create_comunitario(self):
        idEstudiante = self.test_create_estudiante()
        comunitario = {
            'idProyecto': self.faker.random_number(digits=3),
            'nombre_proyecto': self.faker.word(),
            "agno_experiencia": self.faker.random_number(digits=3),
            "lider_proyecto": self.faker.name(),
            "idEstudiante": [idEstudiante],
            # "tareas_impacto": "tareas_impacto",
            # "tareas_extensionista": "tareas_extensionista",
        }

        url = '/gestion/comunitario/'
        response = self.client.post(url, comunitario, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.idProyecto = response.data['idProyecto']
        return self.idProyecto

    def test_update_comunitario(self):
        idProyecto = self.test_create_comunitario()
        idEstudiante = self.test_create_estudiante()
        comunitario = {
            'idProyecto': self.faker.random_number(digits=3),
            'nombre_proyecto': self.faker.word(),
            "agno_experiencia": self.faker.random_number(digits=3),
            "lider_proyecto": self.faker.name(),
            "idEstudiante": [idEstudiante],
            # "tareas_impacto": "tareas_impacto",
            # "tareas_extensionista": "tareas_extensionista",
        }
        url = '/gestion/comunitario/'
        response = self.client.put(url+str(idProyecto)+'/', comunitario, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_comunitario(self):
        response = self.client.get("/gestion/comunitario/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_comunitario(self):
        idProyecto = self.test_create_comunitario()
        response = self.client.get("/gestion/comunitario/"+str(idProyecto)+'/', format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_comunitario(self):
        idProyecto = self.test_create_comunitario()
        response = self.client.delete("/gestion/comunitario/"+str(idProyecto)+'/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#    -----------------------------------------END PROYECTOS COMUNITARIOS----------------------------------------------------------
#    -----------------------------------------BEGIN PROYECTOS DE CÁTEDRA HONORÍFICA----------------------------------------------------------
    def test_create_catedra_honorifica(self):
        idEstudiante = self.test_create_estudiante()
        catedra_honorifica = {
            'idProyecto': self.faker.random_number(digits=3),
            'nombre_proyecto': self.faker.word(),
            "agno_experiencia": self.faker.random_number(digits=3),
            "lider_proyecto": self.faker.name(),
            "idEstudiante": [idEstudiante],
            # "tareas_impacto": "tareas_impacto",
            # "tareas_extensionista": "tareas_extensionista",
        }

        url = '/gestion/catedra_honorifica/'
        response = self.client.post(url, catedra_honorifica, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.idProyecto = response.data['idProyecto']
        return self.idProyecto

    def test_update_catedra_honorifica(self):
        idProyecto = self.test_create_catedra_honorifica()
        idEstudiante = self.test_create_estudiante()
        catedra_honorifica = {
            'idProyecto': self.faker.random_number(digits=3),
            'nombre_proyecto': self.faker.word(),
            "agno_experiencia": self.faker.random_number(digits=3),
            "lider_proyecto": self.faker.name(),
            "idEstudiante": [idEstudiante],
            # "tareas_impacto": "tareas_impacto",
            # "tareas_extensionista": "tareas_extensionista",
        }
        url = '/gestion/catedra_honorifica/'
        response = self.client.put(url+str(idProyecto)+'/', catedra_honorifica, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_catedra_honorifica(self):
        response = self.client.get("/gestion/catedra_honorifica/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_catedra_honorifica(self):
        idProyecto = self.test_create_catedra_honorifica()
        response = self.client.get("/gestion/catedra_honorifica/"+str(idProyecto)+'/', format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_catedra_honorifica(self):
        idProyecto = self.test_create_catedra_honorifica()
        response = self.client.delete("/gestion/catedra_honorifica/"+str(idProyecto)+'/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#    -----------------------------------------END PROYECTOS DE CÁTEDRA HONORÍFICA----------------------------------------------------------
#    -----------------------------------------BEGIN EJERCICIOS INTEGRADORES----------------------------------------------------------
    def test_create_ejercicio_integrador(self):
        idEstudiante = self.test_create_estudiante()
        idAsignatura = self.test_create_asignatura()
        ejercicio_integrador = {
            'idEjercicio_integrador': self.faker.random_number(digits=3),
            'nombre_ejercicio_integrador': self.faker.word(),
            'nota':'5',
            "idEstudiante": [idEstudiante],
            "idAsignatura": [idAsignatura],
        }

        url = '/gestion/ejercicio_integrador/'
        response = self.client.post(url, ejercicio_integrador, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.idEjercicio_integrador = response.data['idEjercicio_integrador']
        return self.idEjercicio_integrador

    def test_update_ejercicio_integrador(self):
        idEjercicio_integrador = self.test_create_ejercicio_integrador()
        idEstudiante = self.test_create_estudiante()
        idAsignatura = self.test_create_asignatura()
        ejercicio_integrador = {
            'idEjercicio_integrador': self.faker.random_number(digits=3),
            'nombre_ejercicio_integrador': self.faker.word(),
            'nota': '2',
            "idEstudiante": [idEstudiante],
            "idAsignatura": [idAsignatura],
        }
        url = '/gestion/ejercicio_integrador/'
        response = self.client.put(url+str(idEjercicio_integrador)+'/', ejercicio_integrador, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_ejercicio_integrador(self):
        response = self.client.get("/gestion/ejercicio_integrador/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_ejercicio_integrador(self):
        idEjercicio_integrador = self.test_create_ejercicio_integrador()
        response = self.client.get("/gestion/ejercicio_integrador/"+str(idEjercicio_integrador)+'/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def t_delete_ejercicio_integrador(self):
        idEjercicio_integrador = self.test_create_ejercicio_integrador()
        response = self.client.delete("/gestion/ejercicio_integrador/"+str(idEjercicio_integrador)+'/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#    -----------------------------------------END EJERCICIOS INTEGRADORES----------------------------------------------------------


    