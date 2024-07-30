from sqlalchemy.orm import Session
from app.models.flight import Flight
from app.schemas.flight import FlightCreate, FlightUpdate

def get_flight(db: Session, flight_id: str):
    return db.query(Flight).filter(Flight.flight_id == flight_id).first()

def get_flights(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Flight).offset(skip).limit(limit).all()

def create_flight(db: Session, flight: FlightCreate):
    db_flight = Flight(**flight.dict())
    db.add(db_flight)
    db.commit()
    db.refresh(db_flight)
    return db_flight

def update_flight(db: Session, flight_id: str, flight: FlightUpdate):
    db_flight = db.query(Flight).filter(Flight.flight_id == flight_id).first()
    if db_flight:
        for key, value in flight.dict(exclude_unset=True).items():
            setattr(db_flight, key, value)
        db.commit()
        db.refresh(db_flight)
    return db_flight

def delete_flight(db: Session, flight_id: str):
    db_flight = db.query(Flight).filter(Flight.flight_id == flight_id).first()
    if db_flight:
        db.delete(db_flight)
        db.commit()
    return db_flight
