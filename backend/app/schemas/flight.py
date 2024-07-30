from pydantic import BaseModel
from datetime import datetime

class FlightBase(BaseModel):
    flight_id: str
    airline: str
    status: str
    departure_gate: str
    arrival_gate: str
    scheduled_departure: datetime
    scheduled_arrival: datetime
    actual_departure: datetime | None = None
    actual_arrival: datetime | None = None

class FlightCreate(FlightBase):
    pass

class FlightUpdate(FlightBase):
    pass

class Flight(FlightBase):
    class Config:
        orm_mode = True
