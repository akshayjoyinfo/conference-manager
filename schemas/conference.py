from pydantic import BaseModel
from datetime import datetime


class CreateConferenceCommand(BaseModel):
    title: str
    description: str
    start_date: datetime
    end_date: datetime


class ConferenceInDBBase(BaseModel):
    id: int
    title: str
    description: str
    start_date: datetime
    end_date: datetime

    class Config:
        orm_mode = True


# Properties to return to client
class ConferenceResponse(ConferenceInDBBase):
    pass
