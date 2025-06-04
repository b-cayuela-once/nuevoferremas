________________________________________
* PASOS PARA UTILIZAR PROYECTO Y ALGUNOS COMANDOS DE UTILIDAD.
________________________________________
- Antes de clonar el repositorio, debes:

* Crear el entorno virtual:
python -m venv env

* Activar entorno virtual en Windows:
.\env\Scripts\activate

* Activar entorno virtual en macOS/Linux:
source env/bin/activate

________________________________________
- Posterior a la creación del entorno virtual, debes:

* Instalar Python:
Instalar desde https://www.python.org/downloads/
Recuerda añadir al Path

* Verificar instalación de python y de pip
python --version
pip --version

________________________________________
- Para poder clonar el repositorio, debes:

* Configurar Git:
git config --global user.name "Tu Nombre"
git config --global user.email "tunombre@ejemplo.com"

* Clonar repositorio:
git clone https://github.com/b-cayuela-once/nuevoferremas.git

________________________________________
- Este paso puede ser ignorado (instalar Django) si clonaste el repositorio, solo debes instalar los requirements y seguir con los demas pasos.

* Instalar Django:
pip install django

* Instalar requirements:
pip install -r requirements.txt

* Actualizar Pip en caso de ser necesario:
python.exe -m pip install --upgrade pip

* Realizar migraciones:
python manage.py makemigrations

* Migrar:
python manage.py migrate

* Crear superusuario:
python manage.py createsuperuser

________________________________________
- En este paso ya debes poder acceder a la base de datos django y tener el proyecto en tu pc.
- Si quieres subir tus avances al github, debes:

* Establecer git en tu proyecto base:
git init 

* Establecer repositorio:
git remote add origin https://github.com/b-cayuela-once/nuevoferremas.git

* Crear requirements.txt:
pip freeze > requirements.txt

* Agregar todos los cambios:
git add .

* Commitear:
git commit -m "Nombre del commit"

* Subir al repositorio:
git push -u origin main

________________________________________
- Algunos comandos de django:

* Arrancar servidor:
python manage.py runserver

* Crear Aplicación:
python manage.py startapp "nombre app"

* Crear superusuario:
python manage.py createsuperuser

________________________________________