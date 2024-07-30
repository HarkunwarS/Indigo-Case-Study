from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.notification import Notification
from app.crud.notification import get_notifications
from app.database import get_db

router = APIRouter()

@router.get("/{flight_id}", response_model=List[Notification])
def read_notifications(flight_id: str, db: Session = Depends(get_db)):
    notifications = get_notifications(db=db, flight_id=flight_id)
    if notifications is None:
        raise HTTPException(status_code=404, detail="No notifications found for this flight")
    return notifications
