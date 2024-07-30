from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.booking import BookingCreate, Booking
from app.crud.booking import create_booking, get_booking, delete_booking
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=Booking)
def book_flight(booking: BookingCreate, db: Session = Depends(get_db)):
    return create_booking(db=db, booking=booking)

@router.delete("/{booking_id}", response_model=Booking)
def cancel_booking(booking_id: int, db: Session = Depends(get_db)):
    db_booking = delete_booking(db=db, booking_id=booking_id)
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking

@router.get("/{booking_id}", response_model=Booking)
def read_booking(booking_id: int, db: Session = Depends(get_db)):
    db_booking = get_booking(db=db, booking_id=booking_id)
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking
