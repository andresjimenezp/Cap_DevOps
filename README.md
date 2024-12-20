# Proyecto de API con FastAPI, MongoDB y Monitoreo

## Descripción

Este proyecto implementa una API simple utilizando FastAPI y MongoDB, junto con un sistema de monitoreo adicional que verifica el estado de la API. La solución incluye:

1. **API con FastAPI**:
   - **/lista-ordenada**: Ordena una lista de números proporcionada por el usuario y devuelve la lista ordenada junto con la hora del sistema.
   - **/healthcheck**: Verifica el estado de la API devolviendo "OK".
   - **/guardar-lista-no-ordenada**: Guarda una lista no ordenada en una base de datos MongoDB con un identificador único (UUID4) y la hora del sistema.

2. **Monitoreo con `api-monitor`**:
   - Verifica periódicamente el estado de la API a través del endpoint `/healthcheck`.
   - Registra los resultados en un archivo de logs.

3. **Configuración basada en contenedores**:
   - Los servicios de la API, MongoDB y el monitoreo se ejecutan en contenedores Docker.
   - Uso de redes Docker para la comunicación entre servicios.

## Requisitos

- Docker
- Docker Compose
- Python 3.9 o superior

## Configuración inicial

### Crear el archivo `.env`

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables de entorno:

```
MONGODB_HOST=mongodb
MONGODB_PORT=27017
TARGET_CONTAINER_HOST=python-api
TARGET_CONTAINER_PORT=8000
CHECK_INTERVAL=10
TZ=America/Bogota
```

- `MONGODB_HOST` y `MONGODB_PORT`: Configuración de la base de datos MongoDB.
- `TARGET_CONTAINER_HOST` y `TARGET_CONTAINER_PORT`: Dirección y puerto de la API a monitorear.
- `CHECK_INTERVAL`: Intervalo de tiempo (en segundos) entre cada verificación de monitoreo.

Incluye también un archivo de demostración llamado `.env.demo` para que otros desarrolladores puedan configurarlo rápidamente.

### Crear directorios para volúmenes y logs

Crea los directorios necesarios para almacenar datos y registros:

```bash
mkdir -p volumes/logs
```

Asegúrate de que los directorios tengan los permisos correctos:

```bash
chmod -R 777 volumes
```

## Construcción y despliegue

### Construir y ejecutar con Docker Compose

Ejecuta el siguiente comando para levantar todos los servicios (API, MongoDB y monitoreo):

```bash
docker-compose --env-file .env --profile prod up --build
```

Esto creará y ejecutará los contenedores necesarios.

## Uso de la API

### Lista ordenada

Endpoint: `/lista-ordenada`

Ejemplo de uso:

```bash
http://localhost:8000/lista-ordenada?lista_no_ordenada=3,1,4,5,2
```

Resultado esperado:

```json
{
  "lista_ordenada": [1, 2, 3, 4, 5],
  "hora_del_sistema": "2024-12-19T20:00:00"
}
```

### Guardar lista no ordenada

Endpoint: `/guardar-lista-no-ordenada`

Ejemplo de uso:

```bash
http://localhost:8000/guardar-lista-no-ordenada?lista_no_ordenada=5,4,7,2,7,2
```

Resultado esperado:

```json
{
  "mensaje": "Lista guardada exitosamente",
  "id": "550e8400-e29b-41d4-a716-446655440000"
}
```

### Verificar el estado de la API

Endpoint: `/healthcheck`

Ejemplo de uso:

```bash
http://localhost:8000/healthcheck
```

Resultado esperado:

```json
"OK"
```

## Monitoreo

El contenedor `api-monitor` verifica periódicamente el estado del endpoint `/healthcheck` y registra los resultados en el archivo de logs ubicado en `volumes/logs/api-monitor.log`.

### Inspeccionar los logs de monitoreo

Puedes revisar los logs directamente desde el contenedor:

```bash
docker exec -it api-monitor cat /opt/api-monitor/logs/api-monitor.log
```

O desde el host:

```bash
cat volumes/logs/api-monitor.log
```

### Configurar el intervalo de verificación

Puedes ajustar el intervalo de verificación modificando la variable `CHECK_INTERVAL` en el archivo `.env`.

4. **Conflictos de puertos**:
   - Cambia los puertos en el archivo `docker-compose.yml` si están en uso.

## Versionado

Esta configuración corresponde a la versión `v2.1.0`, que incluye:

1. Integración del sistema de monitoreo (`api-monitor`).
2. Uso de archivos `.env` para configuración.
3. Configuración de volúmenes persistentes para datos y logs.
4. Documentación actualizada y mejoras en el despliegue.

---
