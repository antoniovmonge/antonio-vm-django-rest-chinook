# Django REST Framework - Chinook API

## Visión General

Este proyecto proporciona una API RESTful para la base de datos Chinook. Se trata de una base de datos de muestra que representa una tienda de medios digitales que incluye tablas para artistas, álbumes, tracks, empleados y más. Está construido con Django y Django REST Framework.

## Características

- Endpoints de API RESTful para acceder a artistas, álbumes y pistas.
- Soporte para paginación.
- Documentación Swagger.
- Contenedorización con Docker y Docker Compose.
- Test suite con Pytest.

## Tabla de Contenidos

### Instalación

Con Docker
Sin Docker

### Documentación de la API

- Listar todos los artistas
- Obtener detalles del artista
- Listar todos los álbumes
- Obtener álbumes del artista
- Obtener pistas del álbum
- Obtener resumen del álbum

### Pruebas

### Estructura del Proyecto

---
---

## Levantar el proyecto

1. Clonar el repositorio y cambiar al directorio del proyecto:

    ```bash
    git clone https://github.com/antoniovmonge/django-rest-chinook.git
    cd django-rest-chinook
    ```

2. Levantar el proyecto con **docker-compose**:

    ```bash
    docker-compose up
    ```

3. ℹ️ Variables de entorno.

    Se han incluído variables de entorno que sólo serán utilizables en el entorno de desarrollo en local. Están localizadas en la ruta `.envs/.local/.django`

4. ℹ️ Base de datos.

    Al tratarse de una base de datos muy pequeña y para facilitar la puesta en marcha del proyecto se ha incluído en el repositorio.
    Se trata de una base de datos SQLite que se encuentra en la ruta `app/chinook.db`.

## Endpoints requeridos

1. GET /artists/ → Devuelve una lista de todos los músicos / grupos.
2. GET /albums/ → Devuelve una lista de todos los discos con sus canciones.
3. GET /artists/{artist_id}/albums/ → Dado un músico / grupo, devuelve un listado de todos sus
discos.
4. GET /albums/{album_id}/tracks/ → Dado un disco, devuelve un listado de todas las
canciones.
5. GET /albums/summary/ → Devuelve un listado de todos los discos con los siguientes datos
agregados:

    - Nombre del músico / grupo.
    - Número total de canciones.

## Estructura

```bash
django-rest-chinook/
.envs                           # Variables de entorno
│   ├── .local/
│   └── .prod/
├── app/                        # Directorio principal de la aplicación
│   ├── chinook/                # App Chinook (modelos, vistas, serializadores)
│   ├── core/                   # Configuraciones principales del proyecto Django
│   ├── tests/                  # Directorio de pruebas
│   ├── users/                  # Modelo de usuario personalizado
│   ├── conftest.py             # Configuración de Pytest
│   ├── manage.py               # Script de gestión de Django
│   ├── requirements.txt        # Dependencias del proyecto
│   └── chinook.db              # Archivo de base de datos SQLite
├── docker-compose.yml          # Configuración de Docker Compose
├── Makefile                    # Comandos útiles
└── README.md                   # Documentación del proyecto
```
