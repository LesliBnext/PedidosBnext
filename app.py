from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime, timezone
from models import TicketIn, TicketOut
from catalog import CATALOG, CONFIRMATION_FALLBACK
from db import SessionLocal, TicketORM
from id_utils import new_id

app = FastAPI(title="API Tickets (14 tipos) - Pedidos 2025", version="1.0.0")

# ---------------------- FUNCIONES AUXILIARES ----------------------
def _validate_required(data: dict, required: list[str]):
    missing = [r for r in required if data.get(r) in (None, "")]
    if missing:
        raise HTTPException(400, f"Faltan campos requeridos: {', '.join(missing)}")

def build_inc(ticket_id: str) -> str:
    return "INC" + ticket_id[:8]

# ---------------------- CREAR TICKET ----------------------
@app.post("/tickets", response_model=TicketOut)
def create_ticket(body: TicketIn):
    # Normalizar el tipo antes de buscarlo
    normalized_type = body.type.strip().lower().replace(" ", "_")
    meta = CATALOG.get(normalized_type)
    if not meta:
        raise HTTPException(400, "type inválido")

    payload = body.model_dump()
    _validate_required(payload, meta["required"])

    # Generar descripción automática si no se envía
    auto_description = body.description or meta.get("summary", "")
    payload["description"] = auto_description

    ticket_id = new_id()
    inc_number = "INC" + ticket_id[:8]
    created_at = datetime.now(timezone.utc).isoformat()

    # Construir mensaje de confirmación con plantilla específica
    template = meta.get("template") or CONFIRMATION_FALLBACK
    confirmation_text = template.format(
        INC=inc_number,
        GROUP=meta["group"]
    )

    # Guardar en base de datos
    db = SessionLocal()
    try:
        row = TicketORM(
            id=ticket_id,
            type=body.type,
            full_name=body.full_name,
            phone=body.phone,
            sev=meta["sev"],
            classstructureid=meta["classstructureid"],
            classificationid=meta["classificationid"],
            summary=meta["summary"],
            group=meta["group"],
            description=auto_description,
            payload=payload,
        )
        db.add(row)
        db.commit()
    finally:
        db.close()

    return {
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
        "confirmation_text": confirmation_text,
    }

# ---------------------- LISTAR TODOS LOS TICKETS ----------------------
@app.get("/tickets")
def list_tickets():
    """
    Devuelve todos los tickets registrados en la base de datos.
    """
    db = SessionLocal()
    try:
        tickets = db.query(TicketORM).all()
        if not tickets:
            return {"message": "No hay tickets registrados aún."}
        return [
            {
                "id": t.id,
                "inc_number": f"INC{t.id[:8]}",
                "type": t.type,
                "full_name": t.full_name,
                "phone": t.phone,
                "summary": t.summary,
                "group": t.group,
                "created_at": t.created_at,
            }
            for t in tickets
        ]
    finally:
        db.close()

# ---------------------- CONSULTAR TICKET POR ID ----------------------
@app.get("/tickets/{ticket_id}")
def get_ticket(ticket_id: str):
    """
    Busca un ticket por su ID interno o número de incidencia (INC...).
    """
    db = SessionLocal()
    try:
        # Permitir búsqueda por ID o por INC
        if ticket_id.startswith("INC"):
            ticket = db.query(TicketORM).filter(TicketORM.id.like(f"{ticket_id[3:]}%")).first()
        else:
            ticket = db.query(TicketORM).filter(TicketORM.id == ticket_id).first()

        if not ticket:
            raise HTTPException(status_code=404, detail="Ticket no encontrado")
        return ticket.__dict__
    finally:
        db.close()
