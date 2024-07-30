from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class Flight(Base):
    __tablename__ = "flights"
    flight_id = Column(String, primary_key=True, unique=True, index=True)
    airline = Column(String)
    status = Column(String)
    departure_gate = Column(String)
    arrival_gate = Column(String)
    scheduled_departure = Column(DateTime)
    scheduled_arrival = Column(DateTime)
    actual_departure = Column(DateTime, nullable=True)
    actual_arrival = Column(DateTime, nullable=True)

    bookings = relationship("Booking", back_populates="flight")
    notifications=relationship("Notification", back_populates="flight")
