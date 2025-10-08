from fastapi import FastAPI, HTTPException
from datetime import datetime, timezone
from models import TicketIn
from catalog import CATALOG, CONFIRMATION_FALLBACK
from id_utils import new_id
from db import save_ticket, get_all_tickets, get_ticket_by_inc

app = FastAPI(title="API Tickets (Cloudant) - Pedidos Bnext", version="2.1.0")

# ---------------------- FUNCIONES AUXILIARES ----------------------
def _validate_required(data: dict, required: list[str]):
    """
    Valida que todos los campos requeridos estén presentes en el payload.
    """
    missing = [r for r in required if data.get(r) in (None, "")]
    if missing:
        raise HTTPException(400, f"Faltan campos requeridos: {', '.join(missing)}")

def build_inc(ticket_id: str) -> str:
    return "INC" + ticket_id[:8]

# ---------------------- CREAR TICKET ----------------------
@app.post("/tickets")
def create_ticket(body: TicketIn):
    # Normalizar tipo
    normalized_type = body.type.strip().lower().replace(" ", "_")
    meta = CATALOG.get(normalized_type)
    if not meta:
        raise HTTPException(400, "Tipo de ticket inválido")

    payload = body.model_dump()
    _validate_required(payload, meta["required"])

    # Generar descripción automática si no se envía
    auto_description = body.description or meta.get("summary", "")
    payload["description"] = auto_description

    # Crear identificadores
    ticket_id = new_id()
    inc_number = build_inc(ticket_id)
    created_at = datetime.now(timezone.utc).isoformat()

    # Construir mensaje de confirmación con plantilla específica
    template = meta.get("template") or CONFIRMATION_FALLBACK
    confirmation_text = template.format(
        INC=inc_number,
        GROUP=meta["group"]
    )

    # Estructura final del ticket
    ticket_data = {
        "id": ticket_id,
        "inc_number": inc_number,
        "type": body.type,
        "full_name": body.full_name,
        "phone": body.phone,
        "sev": meta["sev"],
        "classstructureid": meta["classstructureid"],
        "classificationid": meta["classificationid"],
        "summary": meta["summary"],
        "group": meta["group"],
        "description": auto_description,
        "payload": payload,
        "created_at": created_at,
        "confirmation_text": confirmation_text
    }

    # Guardar en Cloudant
    save_ticket(ticket_data)

    return ticket_data

# ---------------------- LISTAR TODOS LOS TICKETS ----------------------
@app.get("/tickets")
def list_tickets():
    tickets = get_all_tickets()
    if not tickets:
        return {"message": "No hay tickets registrados aún."}
    return tickets

# ---------------------- CONSULTAR TICKET POR INC ----------------------
@app.get("/tickets/{inc_number}")
def get_ticket(inc_number: str):
    ticket = get_ticket_by_inc(inc_number)
    if not ticket:
        raise HTTPException(404, "Ticket no encontrado")
    return ticket
