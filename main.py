from fastapi import FastAPI
from datetime import datetime
import pytz
import json

app = FastAPI()


@app.get("/lista-ordenada")
def lista_ordenada(lista_no_ordenada: str):
    lista = [int(x) for x in lista_no_ordenada.split(",")]

    # Obtener la hora actual en la zona horaria de Colombia
    zona_horaria_colombia = pytz.timezone("America/Bogota")
    hora_actual = datetime.now(zona_horaria_colombia).strftime("%Y-%m-%d %H:%M:%S")

    lista_ordenada = sorted(lista)

    response = {
        "hora_sistema": hora_actual,
        "lista_ordenada": lista_ordenada
    }

    return json.loads(json.dumps(response, indent=4))


@app.get("/healthcheck")
def healthcheck():
    return "OK"
