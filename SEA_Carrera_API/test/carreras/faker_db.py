from faker import Faker
from apps.carreras.models import Departamento

faker = Faker()
# testCase = TestCase()


class SEACarrera_faker_JSON:

    def build_departamento(self):
        return{
            'idDepartamento': faker.random_number(digits=3),
            'nombre_departamento': faker.word(),
            "area": faker.word()
        }

    def build_bibliografia(self):
        return{
            'idBibliografia': faker.random_number(digits=3),
            'titulo': faker.word(),
            'autor': faker.name(),
            'tipo_texto': faker.word(),
            'formato': faker.word(),
            'disponibilidad': "Si",
            "subido": "Si"
        }

    def build_software(self):
        return{
            'idSoftware': faker.random_number(digits=3),
            'nombre_software': faker.word(),
            'descripcion': faker.word(),
            "licencia": "Si"
        }

    def build_trabajo_diploma(self):
        return{
            'idTrabajo_diploma': faker.random_number(digits=3),
            'titulo': faker.word(),
            'descripcion': faker.word(),
            'informe': "Si",
            'nombre_tutor': faker.name(),
            'opinion_tutor': faker.word(),
            'opinion_oponente': faker.word(),
            'linea': faker.word(),
            "nota": "5"
        }

