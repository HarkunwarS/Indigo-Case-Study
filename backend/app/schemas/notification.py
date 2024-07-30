from pydantic import BaseModel
from datetime import datetime

class NotificationBase(BaseModel):
    flight_id: str
    message: str
    timestamp: datetime
    method: str
    recipient: str

class NotificationCreate(NotificationBase):
    pass

class Notification(NotificationBase):
    id: int

    class Config:
        orm_mode = True
