# FastAPI Sorted List Project

Este proyecto es una API simple construida con FastAPI que ofrece dos endpoints:

1. **/lista-ordenada**: Recibe una lista no ordenada y devuelve la lista ordenada junto con la hora actual en la zona horaria de Colombia.
2. **/healthcheck**: Devuelve un estado "OK" para verificar que la API esté funcionando.

## Archivos Principales

- `main.py`: Define los endpoints de la API.
- `Dockerfile`: Configura el contenedor Docker para ejecutar la API usando Uvicorn.

## Requisitos

- [Docker](https://www.docker.com/get-started) instalado en tu sistema.

## Instrucciones para ejecutar el proyecto

### Construir la imagen Docker

Ejecuta el siguiente comando para construir la imagen Docker:

- docker build -t fastapi-sorted-list .

### Ejecutar el contenedor Docker

Después de construir la imagen, puedes ejecutar el contenedor con el siguiente comando:

- docker run -d -p 8000:8000 fastapi-sorted-list

Esto iniciará la API y la expondrá en http://localhost:8000.

## Probar los endpoints

### Lista ordenada

Puedes acceder al endpoint /lista-ordenada para ordenar una lista de números. Por ejemplo:

Ejemplo:
- http://localhost:8000/lista-ordenada?lista_no_ordenada=3,1,4,5,2

