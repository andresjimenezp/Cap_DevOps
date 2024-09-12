import os
import uuid
from pymongo import MongoClient


# Función para guardar la lista no ordenada en MongoDB
def guardar_mongo_db(lista, hora_actual):
    # Obtener las variables de entorno para la conexión a MongoDB
    mongodb_host = os.getenv("MONGODB_HOST", "localhost")
    mongodb_port = os.getenv("MONGODB_PORT", "27017")

    # Establecer conexión a MongoDB
    client = MongoClient(f"mongodb://{mongodb_host}:{mongodb_port}/")
    db = client["python_app"]  # Base de datos "python_app"
    collection = db["listas_no_ordenadas"]  # Colección "listas_no_ordenadas"

    # Generar un identificador único
    id_unico = str(uuid.uuid4())

    # Documento a guardar en MongoDB
    documento = {
        "id": id_unico,
        "lista_no_ordenada": lista,
        "hora_sistema": hora_actual
    }

    # Insertar el documento en la colección
    collection.insert_one(documento)

    # Devolver el ID generado
    return id_unico
