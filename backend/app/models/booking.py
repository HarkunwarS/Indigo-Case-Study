from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    passenger_name = Column(String, index=True)
    passenger_age = Column(Integer)
    passenger_contact = Column(String)
    passenger_email = Column(String)
    flight_id = Column(String, ForeignKey("flights.flight_id"))

    flight = relationship("Flight", back_populates="bookings")
