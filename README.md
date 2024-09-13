# Proyecto de API con FastAPI y MongoDB

## Descripción

Este proyecto implementa una API simple utilizando FastAPI. La API tiene tres endpoints:

1. **/lista-ordenada**: Toma una lista de números no ordenada como parámetro de consulta, la ordena y devuelve la lista ordenada junto con la hora del sistema.
2. **/healthcheck**: Verifica el estado del API devolviendo la respuesta "OK".
3. **/guardar-lista-no-ordenada**: Guarda una lista no ordenada en una base de datos MongoDB junto con la hora del sistema y un identificador único (UUID4), y devuelve un mensaje de éxito con el ID generado.

El proyecto también está configurado para ejecutarse dentro de un contenedor Docker. Además, se utiliza MongoDB como base de datos, y la API puede conectarse a MongoDB a través de una red Docker.

## Requisitos

- Docker
- MongoDB (se utilizará la imagen oficial de MongoDB en Docker).

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

## Agregar configuración MongoDB

Crea una red Docker llamada mongodb-net que permitirá que los contenedores (API y MongoDB) se comuniquen entre sí:

- docker network create mongodb-net

Busca y utiliza la imagen oficial más pequeña de MongoDB desde Docker Hub para correr MongoDB en un contenedor asociado a la red mongodb-net:

- docker run -d --name mongodb --network mongodb-net -p 27017:27017 mongo:latest

Utiliza el Dockerfile provisto para construir la imagen Docker de la API:

- docker build -t python-api .

Inicia un contenedor basado en la imagen python-api, asociándolo a la red mongodb-net y pasando las variables de entorno necesarias para conectarse a MongoDB:

- docker run -d --name python-api --network mongodb-net -p 8000:8000 \
  -e MONGODB_HOST=mongodb \
  -e MONGODB_PORT=27017 \
  python-api

Puedes acceder al endpoint /guardar-lista-no-ordenada para ordenar una lista de números. Por ejemplo:
- http://localhost:8000/guardar-lista-no-ordenada?lista_no_ordenada=5,4,7,2,7,2

Si deseas visualizar los datos almacenados en MongoDB, puedes utilizar MongoDB Compass o cualquier otra herramienta para conectarte al contenedor MongoDB en el puerto 27017.
