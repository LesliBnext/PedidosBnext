from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class TicketIn(BaseModel):
    type: str = Field(..., description="Uno de los 14 tipos de ticket")
    full_name: str
    phone: str
    description: Optional[str] = None
    mrq_pe: Optional[str] = None
    a_envase: Optional[int] = None
    b_envase: Optional[int] = None
    c_envase: Optional[int] = None
    extra: Dict[str, Any] = {}

class TicketOut(BaseModel):
    id: str
    inc_number: str
    type: str
    full_name: str
    phone: str
    sev: str
    classstructureid: str
    classificationid: str
    summary: str
    group: str
    description: Optional[str]
    payload: Dict[str, Any]
    created_at: str
    confirmation_text: str
