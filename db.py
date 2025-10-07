import requests
from datetime import datetime, timezone
import json

# 🔹 Configuración de conexión directa a IBM Cloudant
CLOUDANT_URL = "https://apikey:OY48qTK4COFQ1E1AkI3GZ158Kl3sVWdEydDZMZHgg45Q@b73163c9-f046-49a0-85d2-ddda7220e0bb-bluemix.cloudantnosqldb.appdomain.cloud"
DB_NAME = "ticketspedidos"  # nombre de la base que creaste en Cloudant

# 🔹 Función para crear (guardar) un ticket
def save_ticket(ticket_data: dict):
    url = f"{CLOUDANT_URL}/{DB_NAME}"
    headers = {"Content-Type": "application/json"}

    # Agregar timestamp al documento
    ticket_data["_id"] = ticket_data.get("id")
    ticket_data["created_at"] = datetime.now(timezone.utc).isoformat()

    response = requests.post(f"{url}", headers=headers, data=json.dumps(ticket_data))

    if response.status_code not in (200, 201):
        print("⚠️ Error al guardar en Cloudant:", response.text)
        raise Exception("No se pudo guardar el ticket en Cloudant")

    return response.json()

# 🔹 Función para obtener todos los tickets
def get_all_tickets():
    url = f"{CLOUDANT_URL}/{DB_NAME}/_all_docs?include_docs=true"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Error al obtener tickets: {response.text}")

    data = response.json()
    docs = [row["doc"] for row in data.get("rows", [])]
    return docs

# 🔹 Función para obtener un ticket específico por su INC
def get_ticket_by_inc(inc_number: str):
    all_tickets = get_all_tickets()
    for t in all_tickets:
        if t.get("inc_number") == inc_number:
            return t
    return None
