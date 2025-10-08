import os
import requests
from dotenv import load_dotenv

load_dotenv()

# === CONFIGURACIÓN DE CLOUDANT ===
CLOUDANT_URL = os.getenv("CLOUDANT_URL", "https://b73163c9-f046-49a0-85d2-ddda7220e0bb-bluemix.cloudantnosqldb.appdomain.cloud")
CLOUDANT_DB = os.getenv("CLOUDANT_DB", "ticketspedidos")
CLOUDANT_USER = os.getenv("CLOUDANT_USER", "b73163c9-f046-49a0-85d2-ddda7220e0bb-bluemix")
CLOUDANT_APIKEY = os.getenv("CLOUDANT_APIKEY", "OY48qTK4COFQ1E1AkI3GZ158Kl3sVWdEydDZMZHgg45Q")

# === ORM SIMPLIFICADO COMPATIBLE CON APP EXISTENTE ===
class TicketORM:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

class SessionLocal:
    """Simula una sesión como SQLAlchemy pero guarda en Cloudant."""
    def __init__(self):
        self.buffer = []

    def add(self, row):
        self.buffer.append(row)

    def commit(self):
        for row in self.buffer:
            url = f"{CLOUDANT_URL}/{CLOUDANT_DB}"
            data = row.__dict__
            response = requests.post(url, auth=(CLOUDANT_USER, CLOUDANT_APIKEY), json=data)
            print(f"📤 POST {url} → {response.status_code}")
            if response.status_code not in (200, 201, 202):
                raise Exception(f"Error al guardar: {response.text}")
        self.buffer.clear()

    def query(self, model):
        # Devuelve un objeto que imita la API de SQLAlchemy
        return CloudantQuery(model)

    def close(self):
        pass


class CloudantQuery:
    def __init__(self, model):
        self.model = model

    def all(self):
        url = f"{CLOUDANT_URL}/{CLOUDANT_DB}/_all_docs?include_docs=true"
        response = requests.get(url, auth=(CLOUDANT_USER, CLOUDANT_APIKEY))
        if response.status_code != 200:
            raise Exception(f"Error al listar: {response.text}")
        data = response.json()
        return [TicketORM(**row["doc"]) for row in data.get("rows", []) if "doc" in row]

    def filter(self, condition):
        # Simula .filter(TicketORM.id == ...)
        key, value = list(condition.items())[0]
        url = f"{CLOUDANT_URL}/{CLOUDANT_DB}/_find"
        selector = {"selector": {key: {"$eq": value}}}
        response = requests.post(url, auth=(CLOUDANT_USER, CLOUDANT_APIKEY), json=selector)
        if response.status_code != 200:
            raise Exception(f"Error al filtrar: {response.text}")
        docs = response.json().get("docs", [])
        return [TicketORM(**doc) for doc in docs]

    def first(self):
        results = self.all()
        return results[0] if results else None