import requests
import json
from datetime import datetime, timezone

# ====================================================
# CONFIGURACIÓN CLOUDANT
# ====================================================

# 🔑 Tus credenciales (reemplaza si cambian en el futuro)
CLOUDANT_USER = "b73163c9-f046-49a0-85d2-ddda7220e0bb-bluemix"
CLOUDANT_APIKEY = "OY48qTK4COFQ1E1AkI3GZ158Kl3sVWdEydDZMZHgg45Q"

# 🌐 URL base de Cloudant con autenticación
CLOUDANT_HOST = f"https://{CLOUDANT_USER}:{CLOUDANT_APIKEY}@{CLOUDANT_USER}.cloudantnosqldb.appdomain.cloud"

# 📁 Nombre de la base de datos (debe existir en tu panel de Cloudant)
DB_NAME = "ticketspedidos"

# ====================================================
# FUNCIONES PRINCIPALES
# ====================================================

def save_ticket(ticket_data: dict):
    """
    Guarda un nuevo ticket en Cloudant.
    """
    url = f"{CLOUDANT_HOST}/{DB_NAME}"
    headers = {"Content-Type": "application/json"}

    # Asegurar campos básicos
    ticket_data["_id"] = ticket_data.get("id")
    ticket_data["created_at"] = datetime.now(timezone.utc).isoformat()

    # Enviar a Cloudant
    response = requests.post(url, headers=headers, data=json.dumps(ticket_data))

    # Log para depuración
    print(f"📤 POST {url}")
    print(f"📦 Payload: {json.dumps(ticket_data, indent=2)}")
    print(f"📥 Cloudant respondió ({response.status_code}): {response.text}")

    if response.status_code not in (200, 201):
        raise Exception(f"Error Cloudant: {response.status_code} - {response.text}")

    return response.json()


def get_all_tickets():
    """
    Devuelve todos los tickets guardados en Cloudant.
    """
    url = f"{CLOUDANT_HOST}/{DB_NAME}/_all_docs?include_docs=true"
    response = requests.get(url)

    print(f"📥 GET {url} → {response.status_code}")

    if response.status_code != 200:
        raise Exception(f"Error Cloudant: {response.status_code} - {response.text}")

    data = response.json()
    return [row["doc"] for row in data.get("rows", [])]


def get_ticket_by_inc(inc_number: str):
    """
    Busca un ticket por su número INC (INCxxxxx).
    """
    tickets = get_all_tickets()
    for t in tickets:
        if t.get("inc_number") == inc_number:
            return t
    return None
