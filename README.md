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
- Python 3.9 o superior

## Instrucciones para ejecutar el proyecto

### Crear el archivo `.env`

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables de entorno:

```
MONGODB_HOST=mongodb
MONGODB_PORT=27017
TZ=America/Bogota
```

Asegúrate de agregar el archivo `.env` al `.gitignore` para evitar subir información sensible al repositorio.

También incluye una versión de demostración del archivo `.env` llamada `.env.demo` para que otros desarrolladores puedan configurarlo rápidamente.

### Construir la imagen Docker

Ejecuta el siguiente comando para construir la imagen Docker de la API:

```bash
docker build -t python-api .
```

### Crear y configurar la red Docker

Crea una red Docker llamada `mongodb-net` para que los contenedores (API y MongoDB) puedan comunicarse:

```bash
docker network create mongodb-net
```

### Crear directorios para volúmenes

Crea los directorios necesarios para la persistencia de datos y logs:

```bash
mkdir -p volumes/logs
```

### Crear y ejecutar los contenedores con docker-compose

Utiliza el archivo `docker-compose.yml` para levantar los servicios. Ejecuta:

```bash
docker-compose --env-file .env --profile prod up --build
```

Esto iniciará los contenedores de MongoDB y la API de Python.

## Probar los endpoints

### Lista ordenada

Puedes acceder al endpoint `/lista-ordenada` para ordenar una lista de números. Por ejemplo:

```bash
http://localhost:8000/lista-ordenada?lista_no_ordenada=3,1,4,5,2
```

### Guardar lista no ordenada

Accede al endpoint `/guardar-lista-no-ordenada` para guardar una lista en MongoDB:

```bash
http://localhost:8000/guardar-lista-no-ordenada?lista_no_ordenada=5,4,7,2,7,2
```

### Verificar el estado de la API

Accede al endpoint `/healthcheck` para comprobar que la API está funcionando:

```bash
http://localhost:8000/healthcheck
```

## Descripción del archivo `docker-compose.yml`

### Servicio `python-api`

- **build**: Contexto para construir la imagen de la API.
- **container_name**: Nombre del contenedor: `python-api`.
- **environment**: Variables de entorno definidas en `.env`.
- **ports**: Expone el puerto `8000`.
- **volumes**:
  - Persistencia de logs: `./volumes/logs/info.log:/opt/python-api/logs/info.log`.
- **networks**: Conectado a la red `mongodb-net`.
- **restart**: Política de reinicio: `always`.
- **depends_on**: Asegura que el servicio `mongodb` esté disponible antes de iniciar.
- **profiles**: Ejecutado en el perfil `prod`.
- **hostname**: Nombre del host asignado: `python-api`.

### Servicio `mongodb`

- **image**: Imagen oficial de MongoDB (`mongo:latest`).
- **container_name**: Nombre del contenedor: `mongodb`.
- **ports**: Expone el puerto `27017` (opcional, para uso con herramientas como MongoDB Compass).
- **volumes**:
  - Persistencia de datos: `mongodb_data:/data/db`.
- **networks**: Conectado a la red `mongodb-net`.
- **restart**: Política de reinicio: `always`.
- **profiles**: Ejecutado en el perfil `prod`.
- **hostname**: Nombre del host asignado: `mongodb`.

## Troubleshooting

- **Problemas de conexión a MongoDB**: Asegúrate de que el contenedor `mongodb` esté funcionando correctamente y que las variables de entorno estén configuradas correctamente.
- **Conflicto de puertos**: Cambia los puertos en el archivo `docker-compose.yml` si están en uso.
- **Permisos para directorios**: Asegúrate de que los directorios creados para los logs y los volúmenes tengan permisos adecuados.

## Etiquetado de versión

Esta configuración corresponde a la versión `v1.1.0`, que incluye:

1. Uso de archivos `.env`.
2. Configuración de volúmenes persistentes para datos y logs.
3. Mejora en la documentación y comandos actualizados.
