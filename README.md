# efi_Python
Proyecto de Gestión de Celulares

Este proyecto es una aplicación web desarrollada con Flask para la gestión de un local de venta de celulares. Permite agregar, editar, eliminar y listar celulares en la base de datos.

Requisitos:
- Python 3.x
- MySQL
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-WTF
- PyMySQL

Instalación:

1. Clonar el repositorio:

   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_PROYECTO>

2. Crear y activar un entorno virtual:

   python3 -m venv venv
   source venv/bin/activate   # En Linux/MacOS
   venv\Scripts\activate      # En Windows

3. Instalar las dependencias:

   pip install Flask Flask-SQLAlchemy Flask-Migrate Flask-WTF PyMySQL

4. Configurar la base de datos:

   Asegúrate de tener MySQL instalado y funcionando. Luego, crea una base de datos llamada celulares (o el nombre que hayas especificado en la configuración).


5. Inicializar la base de datos:

   Crea las tablas en la base de datos utilizando Flask-Migrate.

   flask db init
   flask db migrate -m "Migracion 1"
   flask db upgrade

Ejecución:

1. Activar el entorno virtual:

   source venv/bin/activate   # En Linux/MacOS
   venv\Scripts\activate      # En Windows

2. Iniciar la aplicación:

   flask run --reload

   La aplicación estará disponible en http://127.0.0.1:5000.

Uso:

- Página principal: http://127.0.0.1:5000/ - Muestra la página de inicio.
- Lista de celulares: http://127.0.0.1:5000/lista_celulares - Muestra una lista de todos los celulares en la base de datos.
- Agregar celular: http://127.0.0.1:5000/add_iphone - Permite agregar un nuevo celular.
- Editar celular: http://127.0.0.1:5000/edit_iphone/<id> - Permite editar un celular existente.
- Eliminar celular: http://127.0.0.1:5000/delete_iphone/<id> - Permite eliminar un celular.