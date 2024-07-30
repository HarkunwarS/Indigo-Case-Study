from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    flight_id = Column(String, ForeignKey("flights.flight_id"))
    message = Column(String)
    timestamp = Column(DateTime)
    method = Column(String)
    recipient = Column(String)

    flight = relationship("Flight", back_populates="notifications")
