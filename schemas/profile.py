from pydantic import BaseModel
from datetime import datetime


class CreateProfileCommand(BaseModel):
    username: str
    email: str

class ProfileInDBBase(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True


# Properties to return to client
class SpeakerResponse(ProfileInDBBase):
    pass

class ParticipantResponse(ProfileInDBBase):
    pass
