from sqlalchemy import create_engine, Column, String, DateTime, JSON
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

engine = create_engine("sqlite:///tickets.db", future=True)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
Base = declarative_base()

class TicketORM(Base):
    __tablename__ = "tickets"
    id = Column(String, primary_key=True)
    type = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    sev = Column(String, nullable=False)
    classstructureid = Column(String, nullable=False)
    classificationid = Column(String, nullable=False)
    summary = Column(String, nullable=False)
    group = Column(String, nullable=False)
    description = Column(String)
    payload = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)
