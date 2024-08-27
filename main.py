from fastapi import FastAPI, Query
from datetime import datetime
from typing import List

app = FastAPI()

@app.get("/lista-ordenada")
def lista_ordenada(lista_no_ordenada: List[int] = Query(...)):
    hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lista_ordenada = sorted(lista_no_ordenada)
    return {"hora_sistema": hora_actual, "lista_ordenada": lista_ordenada}

@app.get("/healthcheck")
def healthcheck():
    return "OK"
