from fastapi import FastAPI
from datetime import datetime
import pytz
import json

# Crear una instancia de la aplicación FastAPI
app = FastAPI()

# Definir un endpoint GET en la ruta "/lista-ordenada"
@app.get("/lista-ordenada")
def lista_ordenada(lista_no_ordenada: str):
    # Convertir la lista de números que se pasa como una cadena de texto en una lista de enteros
    lista = [int(x) for x in lista_no_ordenada.split(",")]

    # Obtener la zona horaria de Colombia
    zona_horaria_colombia = pytz.timezone("America/Bogota")
    # Obtener la hora actual en la zona horaria de Colombia y formatearla como una cadena de texto
    hora_actual = datetime.now(zona_horaria_colombia).strftime("%Y-%m-%d %H:%M:%S")

    # Ordenar la lista de números
    lista_ordenada = sorted(lista)

    # Crear un diccionario con la hora actual y la lista ordenada
    respuesta = {
        "hora_sistema": hora_actual,
        "lista_ordenada": lista_ordenada
    }

    # Convertir el diccionario a formato JSON y devolverlo como respuesta
    return json.loads(json.dumps(respuesta, indent=4))

# Definir un endpoint GET en la ruta "/healthcheck" para verificar si la API está activa
@app.get("/healthcheck")
def healthcheck():
    # Devolver el estado "OK" como una respuesta simple
    return "OK"