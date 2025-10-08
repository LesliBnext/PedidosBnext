import os
import requests
from dotenv import load_dotenv

load_dotenv()

# --- Configuración de Cloudant ---
CLOUDANT_URL = os.getenv("CLOUDANT_URL", "https://b73163c9-f046-49a0-85d2-ddda7220e0bb-bluemix.cloudantnosqldb.appdomain.cloud")
CLOUDANT_DB = os.getenv("CLOUDANT_DB", "ticketspedidos")
CLOUDANT_USER = os.getenv("CLOUDANT_USER", "b73163c9-f046-49a0-85d2-ddda7220e0bb-bluemix")
CLOUDANT_APIKEY = os.getenv("CLOUDANT_APIKEY", "OY48qTK4COFQ1E1AkI3GZ158Kl3sVWdEydDZMZHgg45Q")

def save_ticket(ticket):
    """Guarda un ticket en la base de datos Cloudant."""
    url = f"{CLOUDANT_URL}/{CLOUDANT_DB}"
    response = requests.post(url, auth=(CLOUDANT_USER, CLOUDANT_APIKEY), json=ticket)

    # Log en consola y también visible desde FastAPI
    print(f"📤 POST {url}")
    print(f"📦 Payload: {ticket}")
    print(f"📥 Respuesta Cloudant: {response.status_code} - {response.text}")

    if response.status_code not in (200, 201, 202):
        raise Exception(f"⚠️ Error Cloudant: {response.status_code} - {response.text}")

def get_all_tickets():
    """Obtiene todos los documentos de Cloudant."""
    url = f"{CLOUDANT_URL}/{CLOUDANT_DB}/_all_docs?include_docs=true"
    response = requests.get(url, auth=(CLOUDANT_USER, CLOUDANT_APIKEY))
    print(f"📥 GET {url} → {response.status_code}")
    if response.status_code != 200:
        raise Exception(f"⚠️ Error al obtener tickets: {response.text}")
    data = response.json()
    return [row["doc"] for row in data.get("rows", [])]

def get_ticket_by_inc(inc_number: str):
    """Busca un ticket por número de incidencia."""
    url = f"{CLOUDANT_URL}/{CLOUDANT_DB}/_find"
    selector = {"selector": {"inc_number": {"$eq": inc_number}}}
    response = requests.post(url, auth=(CLOUDANT_USER, CLOUDANT_APIKEY), json=selector)
    print(f"🔍 Buscando {inc_number} → {response.status_code}")
    if response.status_code != 200:
        raise Exception(f"⚠️ Error al buscar ticket: {response.text}")
    docs = response.json().get("docs", [])
    return docs[0] if docs else None
