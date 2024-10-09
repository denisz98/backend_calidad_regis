from django.db import models
import os
import re
from django.core.files.storage import FileSystemStorage

class CustomFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if not self.exists(name):
            return name
        basename, ext = os.path.splitext(name)
        counter = 1
        while self.exists(name):
            name = f"{basename} ({counter:03d}){ext}"
            counter += 1
        return name

    def get_valid_name(self, name):
        """
        Devuelve el nombre de archivo proporcionado sin modificar.
        """
        return name

nota = [
	('2', '2'),
	('3', '3'),
	('4', '4'),
	('5', '5'),
]
agno_academico = [
	('1', '1'),
	('2', '2'),
	('3', '3'),
	('4', '4'),
	('5', '5'),
]
agno_carrera = [
	('1-4', '1-4'),
	('1-5', '1-5'),
	('1-6', '1-6'),
]
boolean =  [
	
	('Si', 'Si'),
	('No', 'No')
]

 #Bibliografia
# class Bibliografia(models.Model):
# 	idBibliografia = models.BigAutoField(primary_key=True, verbose_name='ID')
# 	titulo = models.CharField(max_length=50, verbose_name='Título')
# 	autor = models.CharField(max_length=30, verbose_name='Autor')
# 	tipo_texto = models.CharField( max_length=30, blank=True, null=True, verbose_name='Tipo de texto')
# 	formato = models.CharField( max_length=50, blank=True, null=True, verbose_name='Formato')
# 	disponibilidad = models.CharField( max_length=2,choices=(boolean), verbose_name='Disponibilidad')
# 	disponibilidad_virtual = models.CharField(max_length=2, verbose_name='Disponibilidad virtual',choices=(boolean), blank=True, null=True)

# 	class Meta:
# 		db_table = 'bibliografia'
# 		verbose_name = 'Bibliografía'
# 		verbose_name_plural = 'Bibliografías'

# 	def __str__(self):
# 		return self.titulo

	#Software
# class Software(models.Model):
# 	idSoftware = models.BigAutoField(primary_key=True, verbose_name='ID')
# 	nombre_software = models.CharField(max_length=50, verbose_name='Nombre')
# 	descripcion = models.CharField(max_length=50, verbose_name='Descripción')
# 	licencia = models.CharField(max_length=2,choices=(boolean), verbose_name='Licencia')

# 	class Meta:
# 		db_table = 'software'
# 		verbose_name = 'Software'
# 		verbose_name_plural = 'Softwares'

# 	def __str__(self):
# 		return self.nombre_software

 #Departamento
class Departamento(models.Model):
	idDepartamento = models.BigAutoField(primary_key=True, verbose_name='ID')
	nombre_departamento = models.CharField(max_length=30, verbose_name='Nombre')
	facultad = models.CharField(max_length=50, verbose_name='Facultad')
	# plan_trabajo_metodologico = models.FileField(upload_to='documents', storage=CustomFileSystemStorage(), max_length=100,null=True, blank=True, verbose_name='Plan de trabajo metodológico')

	class Meta:
		db_table = 'departamento'
		verbose_name = 'Departamento'
		verbose_name_plural = 'Departamentos'

	def __str__(self):
		return self.nombre_departamento

 #Carrera
class Carrera(models.Model):
	idCarrera = models.BigAutoField(primary_key=True, verbose_name='ID')
	nombre_carrera = models.CharField(max_length=30, verbose_name='Nombre')
	plan_estudio = models.FileField(upload_to='documents', storage=CustomFileSystemStorage(), max_length=100, null= True,blank=True, verbose_name='Plan de estudio')
	modalidad = models.CharField(max_length=20, verbose_name='Modalidad')
	unidades_docente = models.CharField( max_length=50,null=True,blank=True, verbose_name='Unidades docente')
	plan_trabajo_metodologico = models.FileField(upload_to='documents', storage=CustomFileSystemStorage(), max_length=100,null= True, blank=True, verbose_name='Plan de trabajo metodológico')
	estrategia_educativa_carrera = models.FileField(upload_to='documents', storage=CustomFileSystemStorage(), max_length=100,null= True, blank=True, verbose_name='Estrategia educativa carrera')
	estrategia_educativa_agno = models.FileField(upload_to='documents', storage=CustomFileSystemStorage(), max_length=100,null= True, blank=True, verbose_name='Estrategia educativa años')
	estrategia_curricular = models.FileField(upload_to='documents', storage=CustomFileSystemStorage(), max_length=100,null= True, blank=True, verbose_name='Estrategia curricular')

	idDepartamento = models.ForeignKey( Departamento, on_delete=models.CASCADE,null=True, blank=True, verbose_name='Departamento')

	class Meta:
		db_table = 'carrera'
		verbose_name = 'Carrera'
		verbose_name_plural = 'Carreras'

	def __str__(self):
		return self.nombre_carrera


 #Datos_promocion
class Datos_promocion(models.Model):
	idDatos_promocion = models.BigAutoField(primary_key=True, verbose_name='ID')
	agno_academico = models.CharField(max_length=1,choices=(agno_academico), verbose_name='Año académico')
	curso = models.CharField(max_length=10, null=True,blank=True, verbose_name='Curso')
	matricula_inicial = models.IntegerField(verbose_name= 'Matrícula inicial')
	cant_aprobados = models.IntegerField(verbose_name= 'Cantidad de aprobados')
	promocion = models.IntegerField(verbose_name= 'Porciento de promocion')

	idCarrera = models.ForeignKey( Carrera, on_delete=models.CASCADE,null=True, blank=True, verbose_name='Carrera')

	class Meta:
		db_table = 'datos_promocion'
		verbose_name = 'Datos promocion'
		verbose_name_plural = 'Datos promociones'

 #Egresado
class Egresado(models.Model):
	idEgresado = models.BigAutoField(primary_key=True, verbose_name='ID')
	centro_trabajo = models.CharField(max_length=100, verbose_name='Centro trabajo')
	nombre_egresado = models.CharField(max_length=50, null=True,blank=True, verbose_name='Nombre del egresado')
	apellido = models.CharField(max_length=50, null=True,blank=True, verbose_name='Apellidos')
	telefono = models.CharField(max_length=15,null=True,blank=True,verbose_name= 'Número teléfono')
	acciones_seguimiento =  models.FileField(upload_to='documents', storage=CustomFileSystemStorage(), max_length=100,null= True, blank=True, verbose_name='Acciones Seguimiento')
	tipo_superacion = models.CharField(max_length=50, verbose_name='Tipo de superación')

	idCarrera = models.ForeignKey( Carrera, on_delete=models.CASCADE,null=True, blank=True, verbose_name='Carrera')

	class Meta:
		ordering = ['idEgresado']
		db_table = 'egresado'
		verbose_name = 'Egresado'
		verbose_name_plural = 'Egresados'

	def __str__(self):
		return self.nombre_egresado

 #Actividad_superacion
# class Actividad_superacion(models.Model):
# 	idActividad_superacion = models.BigAutoField(primary_key=True, verbose_name='ID')
# 	tipo_superacion = models.CharField(max_length=50, verbose_name='Tipo de superación')
# 	ubicacion = models.CharField(max_length=100, verbose_name='Centro trabajo')
# 	curso = models.CharField(max_length=10, null=True,blank=True, verbose_name='Curso')

# 	idEgresado = models.ManyToManyField( Egresado, blank=True, verbose_name='Egresado')

# 	class Meta:
# 		ordering = ['idActividad_superacion']
# 		db_table = 'actividad_superacion'
# 		verbose_name = 'Actividad superacion'
# 		verbose_name_plural = 'Actividad superaciones'

# 	def __str__(self):
# 		return self.tipo_superacion

 #Trabajador
class Trabajador(models.Model):
	idTrabajador = models.BigAutoField(primary_key=True)
	nombre_trabajador = models.CharField(max_length=255)
	apellido = models.CharField(max_length=255)
	# carnet_identidad = models.CharField(unique=True, max_length=11)
	edad = models.IntegerField()
	# sexo = models.CharField(max_length=255)
	# direccion = models.CharField(max_length=255)
	# telefono = models.CharField(max_length=255)
	titulo_academico = models.CharField(max_length=255,null=True)
	# fecha_graduacion = models.CharField(max_length=255)
	# agno_inicial_trabajador = models.IntegerField()
	# trabajador_departamento = models.CharField(null= True,blank= True, max_length=2,choices=(boolean))
	ujc = models.CharField( max_length=2,choices=(boolean))
	pcc = models.CharField( max_length=2,choices=(boolean))

	class Meta:
		db_table = 'trabajador'
		verbose_name = 'Trabajador'
		verbose_name_plural = 'Trabajadores'

	def __str__(self):
		return self.nombre_trabajador


 #Expediente
class Expediente(models.Model):
	idExpediente = models.BigAutoField(primary_key=True)
	archivo = models.FileField(upload_to='documents', storage=CustomFileSystemStorage(), max_length=100, blank=True)
	
	class Meta:
		db_table = 'expediente'
		verbose_name = 'Expediente'
		verbose_name_plural = 'Expedientes'


 #Posgrado
class Posgrado(models.Model):
	idPosgrado = models.BigAutoField(primary_key=True)
	nombre_posgrado = models.CharField(max_length=255)
	edicion = models.CharField(max_length=255)
	fecha_inicio_edicion = models.CharField(max_length=10)
	programa =  models.FileField(upload_to='documents', storage=CustomFileSystemStorage(), max_length=100,null=True, blank=True)
	fecha_culminacion_edicion = models.CharField(max_length=10)
	reconocimiento = models.CharField(max_length=255)
	matricula_inicial_edicion = models.IntegerField()
	matricula_final_edicion = models.IntegerField()
	convenio = models.CharField(max_length=255)
	categoria_cientifica = models.CharField(max_length=255)
	tipo_posgrado = models.CharField(max_length=255)
	encuesta_satisfaccion =  models.FileField(upload_to='documents', storage=CustomFileSystemStorage(), max_length=100,null=True, blank=True)
	
	idExpediente = models.OneToOneField( Expediente,null= True, blank=True, on_delete=models.CASCADE, verbose_name='Expediente')
 
	class Meta:
		db_table = 'posgrado'
		verbose_name = 'Posgrado'
		verbose_name_plural = 'Posgrados'

	def __str__(self):
		return self.nombre_posgrado

# Cargo_metodologico
class Cargo_metodologico(models.Model):
	idCargo_metodologico = models.BigAutoField(primary_key=True, verbose_name='ID')
	cargo = models.CharField(max_length=50, null=True,blank=True, verbose_name='Cargo')

	class Meta:
		db_table = 'cargo_metodologico'
		verbose_name = 'Cargo_metodologico'
		verbose_name_plural = 'Cargo_metodologicos'
	
	def __str__(self):
		return self.cargo
  
 #Profesor
class Profesor(Trabajador, models.Model):
	cargo_direccion = models.CharField(null= True,blank= True, max_length=255)
	# cargo_metodologico = models.CharField(max_length=255)
	graduado_de = models.CharField(max_length=255)
	doctor = models.CharField(max_length=255)
	categoria_docente = models.CharField(max_length=255)
	# fecha_ingreso = models.CharField(max_length=10)
	agnos_exp_educ_superior = models.IntegerField()
	# tutor = models.CharField(null= True,blank= True,max_length=2,choices=(boolean), verbose_name='Tutor')
	ppa = models.CharField(null= True,blank= True, max_length=2,choices=(boolean), verbose_name='PPA')
	guia = models.CharField(null= True,blank= True, max_length=2,choices=(boolean), verbose_name='Guía')
	jefe_diciplina = models.CharField(null= True,blank= True, max_length=2,choices=(boolean), verbose_name='Jefe de disciplina')
	jefe_carrera = models.CharField(null= True,blank= True,max_length=2,choices=(boolean), verbose_name='Jefe de carrera')
	jefe_departamento = models.CharField(null= True,blank= True, max_length=2,choices=(boolean), verbose_name='Jefe de departamento')
	tiempo_parcial = models.CharField(null= True,blank= True, max_length=2,choices=(boolean), verbose_name='Profesor tiempo parcial')
	otras_funciones = models.CharField(max_length=255)
	
	idCargo_metodologico = models.ManyToManyField(Cargo_metodologico, blank=True, through='Profesor_cargo_metodologico', verbose_name='Cargo_metodologico')
	idPosgrado = models.ManyToManyField(Posgrado, blank=True,through='Profesor_posgrado', verbose_name='Nombre del posgrado')

	class Meta:
		db_table = 'profesor'
		verbose_name = 'Profesor'
		verbose_name_plural = 'Profesores'

	def __str__(self):
		return self.nombre_trabajador

# Profesor_cargo_metodologico
class Profesor_cargo_metodologico(models.Model):
	idProfesor_cargo_metodologico = models.BigAutoField(primary_key=True, verbose_name='ID')
	idTrabajador = models.ForeignKey(Profesor,null=True,blank=True, on_delete=models.CASCADE, verbose_name='Profesor')
	idCargo_metodologico = models.ForeignKey(Cargo_metodologico,null=True,blank=True, on_delete=models.CASCADE, verbose_name='Cargo_metodologico')
	curso = models.CharField(max_length=10, null=True,blank=True, verbose_name='Curso')


	class Meta:
		db_table = 'profesor_cargo_metodologico'
		verbose_name = 'Profesor_cargo_metodologico'
		verbose_name_plural = 'Profesor_cargo_metodologicos'

# Profesor_posgrado
class Profesor_posgrado(models.Model):
	idProfesor_posgrado= models.BigAutoField(primary_key=True, verbose_name='ID')
	idTrabajador = models.ForeignKey(Profesor,null=True,blank=True, on_delete=models.CASCADE, verbose_name='Profesor')
	idPosgrado = models.ForeignKey(Posgrado,null=True,blank=True, on_delete=models.CASCADE, verbose_name='Posgrado')
	curso = models.CharField(max_length=10, null=True,blank=True, verbose_name='Curso')

	class Meta:
		db_table = 'profesor_posgrado'
		verbose_name = 'Profesor_posgrado'
		verbose_name_plural = 'Profesor_posgrados'
#Disciplina
class Disciplina(models.Model):
	idDisciplina = models.BigAutoField(primary_key=True, verbose_name='ID')
	nombre_disciplina = models.CharField(max_length=50)
	plan_trabajo_metodologico = models.FileField(upload_to='documents', storage=CustomFileSystemStorage(), max_length=100,null= True, blank=True, verbose_name='Plan de trabajo metodológico')

	jefe =  models.ManyToManyField(Profesor,blank=True,through='Profesor_disciplina', verbose_name='Jefe')
	idCarrera = models.ForeignKey(Carrera, on_delete=models.CASCADE,null=True, blank=True, verbose_name='Carrera')

	class Meta:
		db_table = 'disciplina'
		verbose_name = 'Disciplina'
		verbose_name_plural = 'Disciplinas'

	def __str__(self):
		return self.nombre_disciplina


#Profesor_disciplina

class Profesor_disciplina(models.Model):
	idProfesor_disciplina = models.BigAutoField(primary_key=True, verbose_name='ID')
	idTrabajador = models.ForeignKey(Profesor,null=True,blank=True, on_delete=models.CASCADE, verbose_name='Profesor')
	idDisciplina = models.ForeignKey(Disciplina,null=True,blank=True, on_delete=models.CASCADE, verbose_name='Disciplina')
	curso = models.CharField(max_length=10, null=True,blank=True, verbose_name='Curso')

	class Meta:
		db_table = 'profesor_disciplina'
		verbose_name = 'Profesor_disciplina'
		verbose_name_plural = 'Profesor_disciplinas'
#Alumno ayudante
class Alumno_ayudante(models.Model):
	idAlumno_ayudante = models.BigAutoField(primary_key=True, verbose_name='ID')
	nombre_alumno_ayudante = models.CharField(max_length=50, verbose_name='Nombre')
	apellido = models.CharField(max_length=50, verbose_name='Apellido')
	agno_academico = models.CharField(max_length=1, choices=(agno_academico), verbose_name='Año académico')
	plan = models.FileField(upload_to='documents', max_length=100, blank=True,storage=CustomFileSystemStorage())
	# idAsignatura = models.ManyToManyField(Asignatura,through='Alumno_ayudante_Asignatura',blank=True, verbose_name='Asignatura')
	
	class Meta:
		db_table = 'alumno_ayudante'
		verbose_name = 'Alumno ayudante'
		verbose_name_plural = 'Alumnos ayudantes'
	

 #Asignatura
class Asignatura(models.Model):
	idAsignatura = models.BigAutoField(primary_key=True, verbose_name='ID')
	nombre_asignatura = models.CharField(max_length=50,blank=True, null=True, verbose_name='Nombre')
	# cant_horas = models.IntegerField( verbose_name='Cantidad de horas', blank=True, null=True)
	# horas_totales = models.IntegerField(verbose_name='Horas totales', blank=True, null=True)
	# tipo_curriculum = models.CharField( max_length=50, blank=True, null=True, verbose_name='Tipo de curriculum')
	tipo_evaluacion_final = models.CharField(max_length=50, blank=True, null=True, verbose_name='Tipo de evaluación final')
	asig_virtual = models.CharField(max_length=2, choices=(boolean), verbose_name='Virtual', blank=True, null=True)
	agno_academico = models.CharField(max_length= 1,blank=True, null=True,choices=(agno_academico), verbose_name='Año')
	# objetivo = models.CharField(max_length=100, blank=True, null=True, verbose_name='Objetivo')
	# control_realizado = models.IntegerField( blank=True, null=True,verbose_name='Controles realizados')
	# resultado_control_realizado = models.CharField(max_length=15, blank=True, null=True, verbose_name='Resultado del control realizado')
	programa =  models.FileField(upload_to='documents', storage=CustomFileSystemStorage(), blank=True)

	idDisciplina = models.ForeignKey( Disciplina, verbose_name='Disciplina', blank=True, null=True ,on_delete=models.CASCADE)
	idTrabajador = models.ManyToManyField(Profesor,through='Asignatura_profesor', verbose_name='Profesor', blank=True)
	# idBibliografia = models.ManyToManyField(Bibliografia , blank=True, verbose_name='Bibliografía')
	# idSoftware = models.ManyToManyField(Software , blank=True, verbose_name='Software')
	# idAlumno_ayudante  = models.ManyToManyField( Alumno_ayudante, verbose_name='Alumno ayudante',blank=True)
	idAlumno_ayudante  = models.ManyToManyField( Alumno_ayudante, verbose_name='Alumno ayudante',blank=True)


	class Meta:
		db_table = 'asignatura'
		verbose_name = 'Asignatura'
		verbose_name_plural = 'Asignaturas'

	def __str__(self):
		return self.nombre_asignatura


#Asignatura_profesor
class Asignatura_profesor(models.Model):
	idAsignatura_profesor = models.BigAutoField(primary_key=True, verbose_name='ID')
	idAsignatura = models.ForeignKey(Asignatura, verbose_name='Asignatura', blank=True, null=True ,on_delete=models.CASCADE)
	idTrabajador = models.ForeignKey(Profesor, verbose_name='Profesor', blank=True, null=True ,on_delete=models.CASCADE)
	curso = models.CharField( max_length=15, verbose_name='Curso')

	class Meta:
		db_table = 'asignatura_profesor'
		verbose_name = 'Asignatura profesor'
		verbose_name_plural = 'Asignatura profesores'
  
 #Practica_laboral
class Practica_laboral(Asignatura, models.Model):
	tema_practica_laboral = models.CharField(max_length=50, verbose_name='Tema', blank=True, null=True)
	lugar_ubicacion = models.CharField(max_length=50, verbose_name='Lugar de la ubicación', blank=True, null=True)
	nota = models.CharField(max_length=1, choices=(nota), verbose_name='Nota')

	class Meta:
		db_table = 'practica_laboral'
		verbose_name = 'Práctica laboral'
		verbose_name_plural = 'Práctica laborales'

	def __str__(self):
		return self.tema_practica_laboral


 #Asignatura_virtual
class Asignatura_virtual(Asignatura, models.Model):

	class Meta:
		db_table = 'asignatura_virtual'
		verbose_name = 'Asignatura_virtual'
		verbose_name_plural = 'Asignatura_virtual'


 #Estudiante
class Estudiante(models.Model):
	idEstudiante = models.BigAutoField(primary_key=True, verbose_name='ID')
	nombre_estudiante = models.CharField(max_length=50, verbose_name='Nombre')
	apellido = models.CharField(max_length=50, verbose_name='Apellido')
	agno_academico = models.CharField(max_length=11,choices=(agno_academico),verbose_name='Año académico')
	disponibilidad_tecnologica = models.CharField( max_length=2,choices=(boolean), verbose_name='Disponibilidad tecnológica')
	acceso_wifi = models.CharField( max_length=2,choices=(boolean), verbose_name='Acceso Wifi')
	becado = models.CharField( max_length=2,choices=(boolean), verbose_name='Becado')

	# idAsignatura = models.ManyToManyField(Asignatura,blank=True,through='Asignatura_estudiante_ejIntegrador', verbose_name='Asignatura')
	#idAsignatura = models.ManyToManyField(Trabajo_diploma,blank=True,through='Asignatura_estudiante_ejIntegrador')

	class Meta:
		db_table = 'estudiante'
		verbose_name = 'Estudiante'
		verbose_name_plural = 'Estudiantes'

	def __str__(self):
		return self.nombre_estudiante

 #Trabajo_diploma
class Trabajo_diploma(models.Model):
	idTrabajo_diploma = models.BigAutoField(primary_key=True, verbose_name='ID')
	titulo = models.CharField(max_length=30, verbose_name='Título')
	descripcion = models.CharField(max_length=100, verbose_name='Descripción')
	informe =  models.FileField(upload_to='documents', storage=CustomFileSystemStorage(), blank=True)
	opinion_tutor = models.CharField(max_length=50, verbose_name='Opinión del tutor')
	opinion_oponente = models.CharField(max_length=50, verbose_name='Opinión del oponente')
	linea = models.CharField(max_length=50, verbose_name='Línea')
	nota = models.CharField(max_length=1,choices=(nota),verbose_name='Nota')
	aval =  models.FileField(upload_to='documents', storage=CustomFileSystemStorage(), max_length=100, blank=True)

	idTrabajador = models.ManyToManyField (Profesor, through='Trab_diploma_profesor_estudiante', blank=True, verbose_name='Nombre del tutor')
	idEstudiante = models.ManyToManyField (Estudiante, through='Trab_diploma_profesor_estudiante', blank=True, verbose_name='Estudiante')


	class Meta:
		db_table = 'trabajo_diploma'
		verbose_name = 'Trabajo de diploma'
		verbose_name_plural = 'Trabajos de diplomas'

	def __str__(self):
		return self.titulo


#Trab_diploma_profesor_estudiante

class Trab_diploma_profesor_estudiante(models.Model):
	idTrab_diploma_profesor_estudiante = models.BigAutoField(primary_key=True, verbose_name='ID')
	idTrabajador = models.ForeignKey(Profesor,null=True,blank=True, on_delete=models.CASCADE, verbose_name='Profesor')
	idEstudiante = models.ForeignKey(Estudiante,null=True,blank=True, on_delete=models.CASCADE, verbose_name='Estudiante')
	idTrabajo_diploma = models.ForeignKey(Trabajo_diploma,null=True,blank=True, on_delete=models.CASCADE, verbose_name='Trabajo de diploma')
	curso = models.CharField(max_length=10,null=True, blank= True,verbose_name='Curso')


	class Meta:
		db_table = 'trab_diploma_profesor_estudiante'
		verbose_name = 'Trab_diploma_profesor_estudiante'
		verbose_name_plural = 'Trab_diploma_profesor_estudiantes'

	

 #Ejercicio_integrador
class Ejercicio_integrador(models.Model):
	idEjercicio_integrador = models.BigAutoField(primary_key=True)
	nombre_ejercicio_integrador = models.CharField( max_length=30, verbose_name='Nombre')
	informe =models.FileField( upload_to='documents', storage=CustomFileSystemStorage(), max_length=100,null=True, blank=True, verbose_name='Informe')
	idAsignatura = models.ManyToManyField(Asignatura,blank=True,through='Asignatura_ejIntegrador', verbose_name='Asignatura')

	class Meta:
		db_table = 'ejercicio_integrador'
		verbose_name = 'Ejercicio integrador'
		verbose_name_plural = 'Ejercicios integradores'

	def __str__(self):
		return self.nombre_ejercicio_integrador

 #Asignatura_ejIntegrador
class Asignatura_ejIntegrador(models.Model):
	idAsignatura_ejIntegrador = models.BigAutoField(primary_key=True, verbose_name='ID')
	# nota = models.CharField(max_length=1, choices=(nota),verbose_name='Nota')
	curso = models.CharField(max_length=10, verbose_name='Curso')

	# idEstudiante = models.ForeignKey( Estudiante, verbose_name='Estudiante',null=True,blank=True, on_delete=models.CASCADE)
	idAsignatura = models.ForeignKey(Asignatura, verbose_name='Asignatura',null=True,blank=True, on_delete=models.CASCADE)
	idEjercicio_integrador = models.ForeignKey(Ejercicio_integrador, verbose_name='Ejercicio integrador',null=True,blank=True, on_delete=models.CASCADE)


#Laboratorio
class Laboratorio(models.Model):
	idLaboratorio = models.BigAutoField(primary_key=True, verbose_name='ID')
	numero = models.IntegerField( verbose_name='Número')
	total_pc = models.CharField(max_length=50, verbose_name='Total PC')
	disp_tecnica =models.FileField( upload_to='documents', storage=CustomFileSystemStorage(), max_length=100,null=True, blank=True, verbose_name='Disponibilidad Técnica')

	idCarrera = models.ForeignKey( Carrera,null=True,blank=True, verbose_name='Carrera', on_delete=models.CASCADE)

	class Meta:
		db_table = 'laboratorio'
		verbose_name = 'Laboratorio'
		verbose_name_plural = 'Laboratorios'

	def __str__(self):
		return self.numero

 #Proyecto
class Proyecto(models.Model):
	idProyecto = models.BigAutoField(primary_key=True, verbose_name='ID')
	nombre_proyecto = models.CharField(max_length=50, verbose_name='Nombre')
	# lider_proyecto = models.CharField(max_length=50, verbose_name='Nombre del líder')
	agno_experiencia_lider = models.IntegerField(verbose_name='Año de experiencia')
	tareas_impacto = models.FileField( upload_to='documents', storage=CustomFileSystemStorage(), max_length=100, null= True, blank=True, verbose_name='Tareas de impacto')

	idTrabajador = models.ForeignKey(Profesor, null= True, blank=True,verbose_name='Líder del proyecto' ,on_delete=models.CASCADE)
	idEstudiante = models.ManyToManyField( Estudiante, blank=True, verbose_name='Estudiante')

	class Meta:
		db_table = 'proyecto'
		verbose_name = 'Proyecto'
		verbose_name_plural = 'Proyectos'

	def __str__(self):
		return self.nombre_proyecto

 #Catedra_honorifica
class Catedra_honorifica(Proyecto, models.Model):
	#idCatedra_honorifica = models.BigAutoField(primary_key=True)
	tareas_catedra_honorifica = models.FileField( upload_to='documents', storage=CustomFileSystemStorage(), max_length=100,null= True, blank=True, verbose_name='tareas de catedra honorífica')

	class Meta:
		db_table = 'catedra_honorifica'
		verbose_name = 'Cátedra honorífica'
		verbose_name_plural = 'Cátedras honoríficas'

	def __str__(self):
		return self.nombre_proyecto

 #Investigacion
class Investigacion(Proyecto, models.Model):
	clasificacion = models.CharField(max_length=50, verbose_name='Clasificación')

	class Meta:
		db_table = 'investigacion'
		verbose_name = 'Investigación'
		verbose_name_plural = 'Investigaciones'

	def __str__(self):
		return self.nombre_proyecto

 #Extensionista
class Extensionista(Proyecto, models.Model):
	tareas_extensionista = models.FileField( upload_to='documents', storage=CustomFileSystemStorage(), max_length=100, blank=True,null= True, verbose_name='tareas extensionista')

	class Meta:
		db_table = 'extensionista'
		verbose_name = 'Extensionista'
		verbose_name_plural = 'Extensionistas'

	def __str__(self):
		return self.nombre_proyecto

 #Comunitario
class Comunitario(Proyecto, models.Model):

	tareas_comunitario = models.FileField(upload_to='documents', storage=CustomFileSystemStorage(), max_length=100,null=True, blank=True, verbose_name='tareas comunitarias')

	class Meta:
		db_table = 'comunitario'
		verbose_name = 'Comunitario'
		verbose_name_plural = 'Comunitarios'

	def __str__(self):
		return self.nombre_proyecto


 #EstudiantePosgrado
class Estudiante_posgrado(models.Model):
	idEstudiante_posgrado = models.BigAutoField(primary_key=True)
	nombre_estudiante_posgrado = models.CharField(max_length=255)
	apellido = models.CharField(max_length=255)
	carnet_identidad = models.CharField(max_length=11)
	disponibilidad_tecnologica = models.CharField( max_length=2,choices=(boolean), verbose_name='Disponibilidad tecnológica')
	estudiante_egresado = models.CharField( max_length=2,choices=(boolean), verbose_name='Estudiante egresado')
	
	idExpediente = models.ForeignKey( Expediente, verbose_name='Expediente',null=True,blank=True, on_delete=models.CASCADE)

	class Meta:
		db_table = 'estudiante_posgrado'
		verbose_name = 'Estudiante posgrado'
		verbose_name_plural = 'Estudiante posgrados'

	def __str__(self):
		return self.nombre_estudiante_posgrado

 #Publicacion
class Publicacion(models.Model):
	idPublicacion = models.BigAutoField(primary_key=True)
	titulo = models.CharField(max_length=200,verbose_name='Título')
	fecha_publicacion = models.CharField(max_length=200,verbose_name='Fecha publicación')
	autor = models.CharField(max_length=100, verbose_name='Autor')

	class Meta:
		db_table = 'publicacion'
		verbose_name = 'Publicación'
		verbose_name_plural = 'Publicaciones'

	def __str__(self):
		return self.titulo

 #Ponencia_evento
class Ponencia_evento(models.Model):
	idEvento = models.BigAutoField(primary_key=True)
	nombre_ponencia = models.CharField(max_length=255)
	agno = models.IntegerField()
	tipo_ponencia = models.CharField(max_length=255)
	pais = models.CharField(max_length=255)
 
	idTrabajador = models.ManyToManyField( Profesor, verbose_name='Profesor',blank=True)
	idEstudiante = models.ManyToManyField( Estudiante, verbose_name='Estudiante',blank=True)
	#idPublicacion = models.ManyToManyField(Publicacion, verbose_name='Publicacion')

	class Meta:
		db_table = 'evento'
		verbose_name = 'evento'
		verbose_name_plural = 'Eventos'

	def __str__(self):
		return self.nombre_ponencia



 #Libro
class Libro(Publicacion, models.Model):
	edicion = models.CharField(max_length=255)
	lugar_publicacion = models.CharField(max_length=255)
	editorial = models.CharField(max_length=255)

	class Meta:
		db_table = 'libro'
		verbose_name = 'Libro'
		verbose_name_plural = 'Libros'

	def __str__(self):
		return self.titulo


 #Revista
class Revista(Publicacion, models.Model):
	titulo_revista = models.CharField(max_length=255)
	volumen = models.CharField(max_length=255)
	pagina_inicial = models.CharField(max_length=255)
	pagina_final = models.CharField(max_length=255)
	nivel = models.CharField(max_length=255)
	numero = models.CharField(max_length=255)
	

	class Meta:
		db_table = 'revista'
		verbose_name = 'Revista'
		verbose_name_plural = 'Revistas'

	def __str__(self):
		return self.titulo

 #Memoria_evento
# class Memoria_evento(Publicacion, models.Model):
# 	nombre_editorial = models.CharField(max_length=50, verbose_name='Nombre de la ediorial')
# 	doi = models.CharField(max_length=255,verbose_name='DOI',null=True,blank=True)
# 	isbn = models.CharField(max_length=255, verbose_name='ISBN',null=True,blank=True)
	
# 	idEvento = models.ForeignKey(Evento, verbose_name="Evento",null=True,blank=True, on_delete=models.CASCADE)

# 	class Meta:
# 		db_table = 'memoria_evento'
# 		verbose_name = 'Memoria evento'
# 		verbose_name_plural = 'Memoria eventos'

# 	def __str__(self):
# 		return self.titulo


#  #ProfesorAdjunto
# class Profesor_adjunto(Profesor, models.Model):
# 	centro_trabajo = models.CharField(max_length=255)

# 	class Meta:
# 		db_table = 'profesor_adjunto'
# 		verbose_name = 'Profesor adjunto'
# 		verbose_name_plural = 'Profesores adjuntos'

# 	def __str__(self):
# 		return self.nombre_trabajador

 #Trabajador_no_docente
class Trabajador_no_docente(Trabajador ,models.Model):
	funciones_que_realiza = models.CharField(max_length=255)

	class Meta:
		db_table = 'trabajador_no_docente'
		verbose_name = 'Trabajador no docente'
		verbose_name_plural = 'Trabajadores no docentes'

	def __str__(self):
		return self.nombre_trabajador

 #Premio
class Premio(models.Model):
	idPremio = models.BigAutoField(primary_key=True)
	nombre_premio = models.CharField(max_length=100)
	tipo_premio = models.CharField(max_length=100)
 
	idProfesor = models.ManyToManyField(Profesor, blank=True, verbose_name='Nombre del profesor')
	idEstudiante = models.ManyToManyField(Estudiante, blank=True, verbose_name='Estudiante')

	class Meta:
		db_table = 'premio'
		verbose_name = 'Premio'
		verbose_name_plural = 'Premios'

	def __str__(self):
		return self.tipo_premio
