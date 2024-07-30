import os
from dotenv import load_dotenv
from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth, flight, booking, notification
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

load_dotenv()

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(flight.router, prefix="/flights", tags=["flights"])
app.include_router(booking.router, prefix="/bookings", tags=["bookings"])
app.include_router(notification.router, prefix="/notifications", tags=["notifications"])


TEXTLOCAL_API_KEY = os.getenv("TEXTLOCAL_API_KEY")
TEXTLOCAL_SENDER = os.getenv("TEXTLOCAL_SENDER")
GMAIL_USERNAME = os.getenv("GMAIL_USERNAME")
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")

#print(f"TWILIO_ACCOUNT_SID: {TWILIO_ACCOUNT_SID}")
#print(f"TWILIO_AUTH_TOKEN: {TWILIO_AUTH_TOKEN}")
#print(f"TWILIO_PHONE_NUMBER: {TWILIO_PHONE_NUMBER}")
#print(f"GMAIL_USERNAME: {GMAIL_USERNAME}")
#print(f"GMAIL_PASSWORD: {GMAIL_PASSWORD}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Flight Status and Notifications API"}
