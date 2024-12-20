import os
import time
import logging
import requests

TARGET_CONTAINER_HOST = os.getenv('TARGET_CONTAINER_HOST', 'localhost')
TARGET_CONTAINER_PORT = os.getenv('TARGET_CONTAINER_PORT', '80')
CHECK_INTERVAL = int(os.getenv('CHECK_INTERVAL', 10))
HEALTHCHECK_ENDPOINT = f'http://{TARGET_CONTAINER_HOST}:{TARGET_CONTAINER_PORT}/healthcheck'

logging.basicConfig(
    filename='logs/api-monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def check_health():
    """
    Verifica el estado de salud del contenedor objetivo.
    Registra un mensaje dependiendo del estado de la solicitud.
    """
    try:
        response = requests.get(HEALTHCHECK_ENDPOINT, timeout=5)
        if response.status_code == 200:
            if response.text.strip().upper() == "OK":
                logging.info(f"Solicitud exitosa: {response.status_code}, Respuesta: {response.text}")
            else:
                logging.error(f"Respuesta inesperada: {response.status_code}, Contenido: {response.text}")
        else:
            logging.error(f"Error en la solicitud: Código de estado: {response.status_code}, Respuesta: {response.text}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Fallo la solicitud al endpoint {HEALTHCHECK_ENDPOINT}: {str(e)}")

if __name__ == "__main__":
    while True:
        check_health()
        time.sleep(CHECK_INTERVAL)
