# Data Insight Pro

**Data Insight Pro** es un proyecto inicial para analizar y visualizar perfiles de profesores.
Incluye una estructura básica con Django para la gestión de datos y FastAPI para exponer los endpoints. Centraremos el desarollo del proyecto en iteraciones de MVP.

**Tecnologías Usadas**

- **Django:** Framework para el backend y gestión de datos.
- **FastAPI:** Framework para crear una API RESTful.
- **Frontend:** Implementado con HTML, CSS y JavaScript.

**Estructura del Proyecto**

- `data_insight_pro/`: Carpeta principal del proyecto Django.
- `data/`: Aplicación Django para la carga de datos y gestión de informes.
- `api.py`: Archivo de FastAPI para exponer los endpoints de la API.

**Paso 1: Configuración del Entorno**
- Crear un Proyecto Django
- Configuración de FastAPI

**Paso 2: Desarrollo del Backend**

**2.1. Modelos y Configuración en Django**
- Se define un modelo para almacenar los perfiles de profesores y se migran.
- Se implementa un formulario para cargar archivos CSV en forms.py y una vista para la carga y procesamiento de archivos.
- Se configura el urls.py de la aplicación data, para la vista y se crea la plantilla para el formulario de carga

- Ejecuta el servidor de desarrollo con el siguiente comando:
**python manage.py runserver**
El servidor estará disponible en http://127.0.0.1:8000/.
Nota importante: Aunque el servidor se ejecute, la ruta /upload/ no funcionará correctamente aún, ya que no hemos creado un superusuario ni configurado usuarios o permisos para acceder a esta funcionalidad.

**2.2. Implementación de la API en FastAPI**
- Se definie la API y los endpoints para consultar los datos y generar informes.

- Ejecutar el servidor de FastAPI: Se ha creado un archivo start_uvicorn.py que permite ejecutar el servidor con parámetros configurables, como la activación del modo de recarga automática o el puerto (por ejemplo, el 8080).
Utiliza el siguiente comando:
**python start_uvicorn.py**
El servidor estará disponible en http://127.0.0.1:8080/
Puedes probar el endpoint de la API accediendo a la ruta /professors


