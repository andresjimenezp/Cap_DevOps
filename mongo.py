import os
import uuid
from pymongo import MongoClient

# Función para guardar la lista no ordenada en MongoDB
def guardar_mongo_db(lista, hora_actual):
    """
    Guarda una lista no ordenada y la hora actual en una base de datos MongoDB.

    Argumentos:
    lista: Una lista de números enteros no ordenada.
    hora_actual: Una cadena de texto con la hora actual en formato "YYYY-MM-DD HH:MM:SS".

    Retorna:
    id_unico: Un identificador único (UUID4) generado para el documento guardado.
    """

    # Obtener las variables de entorno para la conexión a MongoDB
    mongodb_host = os.getenv("MONGODB_HOST", "localhost")
    mongodb_port = os.getenv("MONGODB_PORT", "27017")

    # Establecer conexión a MongoDB
    client = MongoClient(f"mongodb://{mongodb_host}:{mongodb_port}/")

    # Seleccionar la base de datos "python_app"
    db = client["python_app"]
    # Seleccionar la colección "listas_no_ordenadas"
    collection = db["listas_no_ordenadas"]

    # Generar un identificador único (UUID4) para el documento
    id_unico = str(uuid.uuid4())

    # Crear el documento a insertar en MongoDB
    documento = {
        "id": id_unico,
        "lista_no_ordenada": lista,
        "hora_sistema": hora_actual
    }

    # Insertar el documento en la colección de MongoDB
    collection.insert_one(documento)

    # Devolver el ID generado para el documento insertado
    return id_unico
