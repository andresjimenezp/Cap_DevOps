from fastapi import FastAPI
from datetime import datetime
import pytz
import json
from mongo import guardar_mongo_db  # Importar la función

app = FastAPI()

# Endpoint para ordenar una lista
@app.get("/lista-ordenada")
def lista_ordenada(lista_no_ordenada: str):
    lista = [int(x) for x in lista_no_ordenada.split(",")]

    zona_horaria_colombia = pytz.timezone("America/Bogota")
    hora_actual = datetime.now(zona_horaria_colombia).strftime("%Y-%m-%d %H:%M:%S")

    lista_ordenada = sorted(lista)

    respuesta = {
        "hora_sistema": hora_actual,
        "lista_ordenada": lista_ordenada
    }

    return json.loads(json.dumps(respuesta, indent=4))

# Nuevo endpoint para guardar la lista no ordenada en MongoDB
@app.get("/guardar-lista-no-ordenada")
def guardar_lista_no_ordenada(lista_no_ordenada: str):
    lista = [int(x) for x in lista_no_ordenada.split(",")]

    zona_horaria_colombia = pytz.timezone("America/Bogota")
    hora_actual = datetime.now(zona_horaria_colombia).strftime("%Y-%m-%d %H:%M:%S")

    # Guardar la lista en MongoDB usando la función importada
    id_unico = guardar_mongo_db(lista, hora_actual)

    # Respuesta de éxito con el ID único
    return {"msg": f"La lista no ordenada fue guardada con el id: {id_unico}"}

# Endpoint para verificar el estado del API
@app.get("/healthcheck")
def healthcheck():
    return "OK"
