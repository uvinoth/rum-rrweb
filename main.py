from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, JSON, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base, Session
import logging

# --------------------------------------------------
# App setup
# --------------------------------------------------

app = FastAPI(
    title="RUM Service",
    description="Real User Monitoring Event Ingestion",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # DEV ONLY
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("rum")

# --------------------------------------------------
# Database setup (SQLite for demo)
# --------------------------------------------------

DATABASE_URL = "sqlite:///./rum.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# --------------------------------------------------
# Database models
# --------------------------------------------------

class Rum(Base):
    __tablename__ = "rum"

    id = Column(Integer, primary_key=True, index=True)
    org_id = Column(Integer, index=True)
    endpoint_id = Column(Integer, index=True)


class RumEvent(Base):
    __tablename__ = "rum_event"

    id = Column(Integer, primary_key=True, index=True)
    org_id = Column(Integer, index=True)
    endpoint_id = Column(Integer, index=True)
    session_id = Column(String)
    event_type = Column(Integer)
    event_data = Column(JSON)
    event_timestamp = Column(Integer)
    url = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(bind=engine)

# --------------------------------------------------
# DTOs (Pydantic models)
# --------------------------------------------------

class EventObject(BaseModel):
    type: int
    data: Dict[str, Any]
    timestamp: int


class EventRequest(BaseModel):
    orgId: int = Field(..., alias="orgId")
    sessionId: Optional[str] = Field(None, alias="sessionId")
    url: Optional[str] = None
    ts: Optional[datetime] = None
    events: List[EventObject]

    class Config:
        allow_population_by_field_name = True



# API endpoint

@app.get("/")
def index():
    with open("index.html") as f:
        return HTMLResponse(f.read())
    

@app.get("/player")
def player():
    with open("player.html") as f:
        return HTMLResponse(f.read())

    
@app.post(
    "/api/v1/rum/events",
    status_code=status.HTTP_201_CREATED,
    tags=["Real User Monitoring"],
)
def rum_events(
    req: EventRequest,
    db: Session = Depends(get_db),
):
    logger.debug("Rum Events data: %s", req.dict())

    print("req.dict()", req.dict())

    # Validate events
    if not req.events:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="no events provided",
        )

    # Validate
    # rum_endpoint = (
    #     db.query(Rum)
    #     .filter(
    #         Rum.org_id == req.orgId
    #     )
    #     .first()
    # )

    # if not rum_endpoint:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail=f"Org '{req.orgId}' not found",
    #     )

    # Default sessionId
    session_id = req.sessionId or "unknown"

    # Save events
    try:
        for event in req.events:
            db_event = RumEvent(
                org_id=req.orgId,
                session_id=session_id,
                event_type=event.type,
                event_data=event.data,
                event_timestamp=event.timestamp,
                url=req.url,
                created_at=req.ts or datetime.utcnow(),
            )
            db.add(db_event)

        db.commit()

    except Exception as exc:
        db.rollback()
        logger.exception("Failed to save events")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="failed to save events",
        ) from exc

    return {
        "message": "events created successfully",
        "events_received": len(req.events),
    }

@app.get(
    "/api/v1/rum/{org}/{sessionId}/events",
    tags=["Real User Monitoring"],
)
def get_session_events(
    org: int,
    sessionId: str,
    db: Session = Depends(get_db),
):
    """
    Get RUM events for a given org and session
    """

    if org <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid Org ID",
        )

    try:
        rows = (
            db.query(RumEvent)
            .filter(
                RumEvent.org_id == org,
                RumEvent.session_id == sessionId,
            )
            .order_by(RumEvent.event_timestamp.asc())  # IMPORTANT for rrweb
            .all()
        )

    except Exception as exc:
        logger.exception("Failed to fetch events")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="failed to fetch error events",
        ) from exc

    if not rows:
        return {
            "events": [],
            "total": 0,
            "session_id": sessionId,
        }

    # Convert DB rows → rrweb event format
    events = [
        {
            "type": row.event_type,
            "data": row.event_data,
            "timestamp": row.event_timestamp,
        }
        for row in rows
    ]

    return {
        "events": events,
        "total": len(events),
        "session_id": sessionId,
    }


