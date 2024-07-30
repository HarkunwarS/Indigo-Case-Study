from pydantic import BaseModel, EmailStr

class BookingBase(BaseModel):
    passenger_name: str
    passenger_age: int
    passenger_contact: str
    passenger_email: EmailStr
    flight_id: str

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    id: int

    class Config:
        orm_mode = True
