________________________________________
* PASOS PARA UTILIZAR PROYECTO.
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

* Instalar Django:
pip install django

* Actualizar Pip en caso de ser necesario:
python.exe -m pip install --upgrade pip

* Realizar migraciones:
python manage.py makemigrations

* Migrar:
python manage.py migrate

* Crear superusuario:
python manage.py createsuperuser
________________________________________
- En este paso ya debes poder acceder a la base de datos django y tener el proyecto.

