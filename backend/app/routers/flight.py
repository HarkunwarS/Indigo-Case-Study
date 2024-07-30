from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.flight import FlightCreate, FlightUpdate, Flight
from app.schemas.notification import NotificationCreate
from app.crud.flight import create_flight, get_flight, get_flights, update_flight, delete_flight
from app.crud.notification import create_notification
from app.database import get_db
from datetime import datetime
from app.models.booking import Booking
from app.utils.notifications import send_sms, send_email

router = APIRouter()

@router.post("/", response_model=Flight)
def create_new_flight(flight: FlightCreate, db: Session = Depends(get_db)):
    return create_flight(db=db, flight=flight)

@router.get("/{flight_id}", response_model=Flight)
def read_flight(flight_id: str, db: Session = Depends(get_db)):
    db_flight = get_flight(db=db, flight_id=flight_id)
    if db_flight is None:
        raise HTTPException(status_code=404, detail="Flight not found")
    return db_flight

@router.put("/{flight_id}", response_model=Flight)
def update_existing_flight(flight_id: str, flight: FlightUpdate, db: Session = Depends(get_db)):
    db_flight = get_flight(db=db, flight_id=flight_id)
    if db_flight is None:
        raise HTTPException(status_code=404, detail="Flight not found")
    
    changes = []
    if flight.status != db_flight.status:
        changes.append(f"Status: {flight.status}")
    if flight.departure_gate != db_flight.departure_gate:
        changes.append(f"Departure gate: {flight.departure_gate}")
    if flight.arrival_gate != db_flight.arrival_gate:
        changes.append(f"Arrival gate: {flight.arrival_gate}")
    if flight.actual_departure != db_flight.actual_departure:
        changes.append(f"Departure time: {flight.actual_departure.strftime('%I:%M %p')}")
    if flight.actual_arrival != db_flight.actual_arrival:
        changes.append(f"Arrival time: {flight.actual_arrival.strftime('%I:%M %p')}")
    
    updated_flight = update_flight(db=db, flight_id=flight_id, flight=flight)
    
    if changes:
        message = f"""
        Hello, greetings from Indigo!

        We are sorry to notify that your travel with flight {flight_id} has some changes.

        Previous details:
        Departure Time: {db_flight.scheduled_departure.strftime("%I:%M %p")}
        Arrival Time: {db_flight.scheduled_arrival.strftime("%I:%M %p")}
        Departure Gate: {db_flight.departure_gate}
        Arrival Gate: {db_flight.arrival_gate}

        New Details:
        Departure Time: {flight.actual_departure.strftime("%I:%M %p")}
        Arrival Time: {flight.actual_arrival.strftime("%I:%M %p")}
        Departure Gate: {flight.departure_gate}
        Arrival Gate: {flight.arrival_gate}

        We are sorry for the inconvenience caused.

        Hope you have a happy journey with Indigo Airlines!
        """
        for passenger in db_flight.bookings:
            notification_sms = NotificationCreate(
                flight_id=flight_id,
                message=message,
                timestamp=datetime.utcnow(),
                method="SMS",
                recipient=passenger.passenger_contact
            )
            notification_email = NotificationCreate(
                flight_id=flight_id,
                message=message,
                timestamp=datetime.utcnow(),
                method="Email",
                recipient=passenger.passenger_email
            )
            create_notification(db=db, notification=notification_sms)
            create_notification(db=db, notification=notification_email)

            # Send notifications directly
            send_sms(notification_sms.recipient, notification_sms.message)
            send_email(notification_email.recipient, "Flight Status Update", notification_email.message)
    
    return updated_flight


@router.get("/", response_model=List[Flight])
def read_flights(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    flights = get_flights(db=db, skip=skip, limit=limit)
    return flights

@router.delete("/{flight_id}", response_model=Flight)
def delete_existing_flight(flight_id: str, db: Session = Depends(get_db)):
    db_flight = delete_flight(db=db, flight_id=flight_id)
    if db_flight is None:
        raise HTTPException(status_code=404, detail="Flight not found")
    return db_flight
