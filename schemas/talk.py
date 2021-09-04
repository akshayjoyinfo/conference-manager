from pydantic import BaseModel
from datetime import datetime


class CreateTalkCommand(BaseModel):
    title: str
    description: str
    talk_date: datetime
    duration: str

class UpdtaeTalkCommand(CreateTalkCommand):
    pass


class TalkInDBBase(BaseModel):
    id: int
    title: str
    description: str
    talk_date: datetime
    duration: str
    conference_id: int


    class Config:
        orm_mode = True


# Properties to return to client
class TalkResponse(TalkInDBBase):
    pass
