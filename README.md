# Django REST Framework - Chinook API

## Tabla de Contenidos

- [Visión General](#visión-general)
- [Características](#características)
- [Puesta en marcha](#puesta-en-marcha)
- [Documentación de la API](#documentación-de-la-api)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Implementación de Cacheing (Redis)](#implementación-de-cacheing-redis)
- [Despliegue en AWS (EC2 o ECS)](#despliegue-en-aws-ec2-o-ecs)

## Visión General

Este proyecto proporciona una API RESTful para la base de datos Chinook. Se trata de una base de datos de muestra que representa una tienda de medios digitales que incluye tablas para artistas, álbumes, tracks, empleados y más.

## Características

- Endpoints de API RESTful para acceder a artistas, álbumes y pistas.
- Soporte para paginación.
- Documentación interactiva con Swagger
- Contenedorización con Docker y Docker Compose.
- Test suite con Pytest

## Puesta en marcha

1. Requisitos:

    - **Docker** y **Docker Compose** previamente instalados.

2. Clonar el repositorio y cambiar al directorio del proyecto:

    ```bash
    git clone https://github.com/antoniovmonge/django-rest-chinook.git
    cd django-rest-chinook
    ```

3. Levantar el proyecto con **docker-compose**:

    ```bash
    docker-compose up
    ```

4. ℹ️ Variables de entorno.

    Se han incluído variables de entorno que sólo serán utilizables en el entorno de desarrollo en local. Están localizadas en la ruta `.envs/.local/.django`

5. ℹ️ Base de datos.

    Al tratarse de una base de datos muy pequeña y para facilitar la puesta en marcha del proyecto se ha incluído en el repositorio.
    Se trata de una base de datos SQLite que se encuentra en la ruta `app/chinook.db`.

## Documentación de la API

ℹ️ Se puede acceder a la documentación Swagger en <http://127.0.0.1:8000/api/v1/schema/swagger-ui/> para explorar la API de forma interactiva.

### Listado de endpoints

1. `GET /artists/` → Devuelve una lista de todos los músicos / grupos.
2. `GET /albums/` → Devuelve una lista de todos los discos con sus canciones.
3. `GET /artists/{artist_id}/albums/` → Dado un músico / grupo, devuelve un listado de todos sus
discos.
4. `GET /albums/{album_id}/tracks/` → Dado un disco, devuelve un listado de todas las
canciones.
5. `GET /albums/summary/` → Devuelve un listado de todos los discos con los siguientes datos
agregados:

    - Nombre del músico / grupo.
    - Número total de canciones.

### Ejemplo de uso de la API

ℹ️ Para probar los endpoints, puedes usar herramientas como Postman o cURL. A continuación se muestran ejemplos de uso con cURL.

#### Listar todos los artistas

Recupera una lista paginada de todos los músicos/grupos.

Endpoint: `GET /api/v1/artists/`

Ejemplo cURL:

```bash
curl -X GET "http://localhost:8000/api/v1/artists/" -H "accept: application/json"
```

Respuesta:

```json
{
  "count": 275,
  "next": "http://localhost:8000/api/v1/artists/?page=2",
  "previous": null,
  "results": [
    {
      "artist_id": 1,
      "name": "AC/DC"
    },
    {
      "artist_id": 2,
      "name": "Accept"
    },
    // ...
  ]
}
```

#### Listar todos los álbumes

Recupera una lista paginada de todos los discos.

Endpoint: `GET /api/v1/albums/`

Ejemplo cURL:

```bash
curl -X GET "http://localhost:8000/api/v1/albums/" -H "accept: application/json"
```

Respuesta:

```json
{
  "count": 347,
  "next": "http://localhost:8000/api/v1/albums/?page=2",
  "previous": null,
  "results": [
    {
      "album_id": 1,
      "title": "For Those About To Rock We Salute You",
      "artist_id": 1
    },
    {
      "album_id": 2,
      "title": "Balls to the Wall",
      "artist_id": 2
    },
    // ...
  ]
}
```

#### Obtener discos del artista

Recupera todos los álbumes de un artista específico.

Endpoint: `GET /api/v1/artists/{artist_id}/albums/`

Ejemplo cURL:

```bash
curl -X GET "http://localhost:8000/api/v1/artists/1/albums/" -H "accept: application/json"
```

Respuesta:

```json
[
  {
    "album_id": 1,
    "title": "For Those About To Rock We Salute You",
    "artist_id": 1
  },
  {
    "album_id": 4,
    "title": "Let There Be Rock",
    "artist_id": 1
  }
]
```

#### Obtener las canciones del disco

Recupera todas las canciones de un disco específico.

Endpoint: `GET /api/v1/albums/{album_id}/tracks/`

Ejemplo cURL:

```bash
curl -X GET "http://localhost:8000/api/v1/albums/1/tracks/" -H "accept: application/json"
```

Respuesta:

```json
[
  {
    "track_id": 1,
    "name": "For Those About To Rock (We Salute You)",
    "albumid": 1,
    "mediatypeid": 1,
    "genre_id": 1,
    "composer": "Angus Young, Malcolm Young, Brian Johnson",
    "milliseconds": 343719,
    "bytes": 11170334,
    "unitprice": "0.99"
  },
  // ... más pistas
]
```

#### Obtener todos los discos con resumen

Recupera un resumen de todos los discos, incluyendo el nombre del artista y el número total de canciones.

Endpoint: `GET /api/v1/albums/summary/`

Ejemplo cURL:

```bash
curl -X GET "http://localhost:8000/api/v1/albums/summary/" -H "accept: application/json"
```

Respuesta:

```json
{
  "count": 347,
  "next": "http://127.0.0.1:8000/api/v1/albums/summary/?page=2",
  "previous": null,
  "results": [
    {
      "album_id": 1,
      "title": "For Those About To Rock We Salute You",
      "artist_name": "AC/DC",
      "total_tracks": 10
    },
    {
      "album_id": 2,
      "title": "Balls to the Wall",
      "artist_name": "Accept",
      "total_tracks": 1
    },
    // ...
  ]
}
```

## Estructura del Proyecto

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

## Implementación de Cacheing (Redis)

Utilizaría un sistema de cacheo para almacenar respuestas de consultas con las siguientes características:

- los datos a los que hace referencia no cambian con frecuencia (Son medianamente estables)
- son de un tamaño considerable o de alto coste computacional
- se hace esa consulta muy a menudo

Esto mejoraría el rendimiento de la API y reduciría la carga en la base de datos.

Añadiría Redis como servicio en el `docker-compose.yml` y configuraría Django para usar Redis como backend de cacheo.

Por ejemplo:

`settings.py`

```python

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# Tiempo de vida del caché (en segundos) - 15 minutos
CACHE_TTL = 60 * 15
```

Luego incorporaría los decoradores a los metodos de vista que quiero cachear:

```python
class MuchosDeEstosView(APIView):
  @method_decorator(cache_page(settings.CACHE_TTL))
  def get(self, request):
    # Lógica de la vista
    pass
```

Así, cada vez que se haga una petición a la vista, Django primero buscará en la memoria caché. Si la respuesta no está en caché, se ejecutará la lógica de la vista y almacenará la respuesta en el caché para las próximas peticiones.

## Despliegue en AWS (EC2 o ECS)

Dadas las carácterísiticas del proyecto haría un despliegue en AWS usando EC2 o ECS (Elastic Container Service).

En lugar de usar SQLite, crearía una configuración para staging y producción que usase PostgreSQL o AWS RDS.

El docker-compose que usaría se llamaría `docker-compose.prod.yml` e incluiría los servicios de PostgreSQL y Nginx.

Si usase ECS subiría las imagenes de Docker a ECR (Elastic Container Registry) y crearía un clúster de ECS para ejecutar los contenedores. Esto es un despliegue manual que intentaría automatizar con Terraform.

En el caso de usar EC2, crearía una instancia EC2 y desplegaría el contenedor Docker directamente en la instancia. Configuraría Nginx como proxy inverso para dirigir el tráfico a la aplicación Django.

A parte de todo esto haría falta configurar un dominio y un certificado SSL para asegurar la comunicación entre el cliente y el servidor. Esto lo haría con AWS Route 53 o NameCheap y AWS Certificate Manager.
