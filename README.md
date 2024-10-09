# Pre-Requisitos para el despliegue
## Instalación de Git
1. Descargar el instalador: https://git-scm.com/download/win
2. Ejecutar el instalador.
3. Descargar el proyecto: git clone https://github.com/IngUniss/tesis_sw_calidad_carrera_2022.git

## Instalación de Python y pip  
1. Descargar el instalador: https://www.python.org/downloads/
2. Ejecutar el instalador.  
3. Elegir Add python.exe to PATH (Añadir Python a PATH).   
4. Seleccionar Install Now (Instalar ahora).
5. Compruebe la versión de Python instalada: `python --version`    
6. Compruebe la versión de pip instalada: `pip --version`    

## Ejecución del entorno virtual   
1. Dentro de la carpeta tesis_sw_calidad_carrera_2022 ejcutar: `source virtualvenv/bin/activate`    

## Instalación de Django
1. Instalar Django: `pip install django`    
2. Compruebe la versión instalada: `python -m django --version`    

## Instalación de dependencias        
1. Instalar Django Rest Framework `pip install djangorestframework`
2. Instalar Rest Framework Simple JWT `pip install djangorestframework-simplejwt`
3. Instalar simple history `pip install django-simple-history`
4. Instalar swagger `pip install drf-yasg`
5. Instalar Psycopg2: `pip install psycopg2` (En caso de error:`pip install psycopg2-binary`)
6. Instalar Faker: `pip install Faker`
7. Instalar corsheaders: `pip install django-cors-headers`

## Instalación de PostgreSQL
1. Descargar PostgreSQL: https://www.postgresql.org/download/windows/    
2. Instalar el archivo descargado    

# Pasos para el despliegue
1. Crear base de datos en PgAdmin con el nombre "SEA_db" y 
2. Crear un archivo .env en la raiz del proyecto con los siguientes valores

        DB_NAME=SEA_db
        DB_USER=<db_user>
        DB_PASSWORD=<db_password>
        DB_HOST=localhost
        DB_PORT=5432

3. Ejecutar una terminal en la carpeta del proyecto, donde se encuentra el archivo "manage.py"
4. Exportar cambios de la base de datos: `python manage.py makemigrations`
5. Migrar base de datos a pgAdmin: `python manage.py migrate`
6. Crear superusuario: `python manage.py createsuperuser`
       
# Para correr el servidor de la apliación  
1. Ejecutar el proyecto `python manage.py runserver`

# Para ejecutar las pruebas de integración   
1. Detener el servidor del proyecto en caso de que esté activo
2. Ejecutar `python manage.py test`