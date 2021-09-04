from typing import List
from pydantic import BaseModel
from datetime import datetime

from .talk import TalkResponse

class CreateConferenceCommand(BaseModel):
    title: str
    description: str
    start_date: datetime
    end_date: datetime

class UpdateConferenceCommand(CreateConferenceCommand):
    pass


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
    talks: List[TalkResponse]

