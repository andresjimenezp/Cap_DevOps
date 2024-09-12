from fastapi import FastAPI
from datetime import datetime
import pytz
import json
from mongo import guardar_mongo_db

# Crea una instancia de la aplicación FastAPI.
app = FastAPI()

# Define un endpoint GET en la ruta "/lista-ordenada" que toma una lista de números como string, la ordena y devuelve la lista ordenada junto con la hora actual del sistema.
@app.get("/lista-ordenada")
def lista_ordenada(lista_no_ordenada: str):
    """
    Recibe una lista no ordenada como una cadena de texto (por ejemplo: "5,3,8,1").
    La convierte en una lista de enteros, la ordena y devuelve un JSON con la lista ordenada y la hora actual.
    """

    # Convierte la lista de números, recibida como una cadena de texto separada por comas, en una lista de enteros.
    lista = [int(x) for x in lista_no_ordenada.split(",")]

    # Obtiene la zona horaria de Colombia (America/Bogota).
    zona_horaria_colombia = pytz.timezone("America/Bogota")
    # Obtiene la hora actual en la zona horaria de Colombia y la formatea como una cadena de texto.
    hora_actual = datetime.now(zona_horaria_colombia).strftime("%Y-%m-%d %H:%M:%S")

    # Ordena la lista de números.
    lista_ordenada = sorted(lista)

    # Crea un diccionario con la lista ordenada y la hora actual del sistema.
    respuesta = {
        "hora_sistema": hora_actual,
        "lista_ordenada": lista_ordenada
    }

    # Convierte el diccionario en formato JSON con una indentación de 4 espacios para que sea más legible.
    return json.loads(json.dumps(respuesta, indent=4))

# Define un nuevo endpoint GET en la ruta "/guardar-lista-no-ordenada" que guarda una lista no ordenada en MongoDB.
@app.get("/guardar-lista-no-ordenada")
def guardar_lista_no_ordenada(lista_no_ordenada: str):
    """
    Recibe una lista no ordenada como una cadena de texto (por ejemplo: "5,3,8,1").
    Guarda la lista en MongoDB con un identificador único y la hora actual, y devuelve un mensaje de éxito con el ID generado.
    """

    # Convierte la lista de números, recibida como una cadena de texto separada por comas, en una lista de enteros.
    lista = [int(x) for x in lista_no_ordenada.split(",")]

    # Obtiene la zona horaria de Colombia (America/Bogota).
    zona_horaria_colombia = pytz.timezone("America/Bogota")
    # Obtiene la hora actual en la zona horaria de Colombia y la formatea como una cadena de texto.
    hora_actual = datetime.now(zona_horaria_colombia).strftime("%Y-%m-%d %H:%M:%S")

    # Guarda la lista no ordenada y la hora del sistema en MongoDB usando la función `guardar_mongo_db`.
    id_unico = guardar_mongo_db(lista, hora_actual)

    # Devuelve un mensaje en formato JSON indicando que la lista fue guardada, incluyendo el identificador único generado.
    return {"msg": f"La lista no ordenada fue guardada con el id: {id_unico}"}

# Define un endpoint GET en la ruta "/healthcheck" para verificar que la API está funcionando correctamente.
@app.get("/healthcheck")
def healthcheck():
    """
    Endpoint para comprobar el estado de la API.
    Simplemente devuelve "OK" si la API está en funcionamiento.
    """

    return "OK"
