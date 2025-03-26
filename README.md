# Django REST Framework - Chinook

API REST para la base de datos "chinook"

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

## Comandos para ejecutar sin Docker

```bash
python app/manage.py test
```

## Comandos ejecutandose en Docker

```bash
docker-compose build
```

```bash
docker-compose up
```

Run Migrations:

```bash
docker compose exec chinook python manage.py migrate --noinput
```

Ejecutar tests:

```bash
docker compose exec web pytest
```
