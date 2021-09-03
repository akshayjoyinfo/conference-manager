from sqlalchemy import Boolean, Column, Integer, String, DateTime, Time, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column

from db.database import Base

from .profile import Participant, Speaker , Profile

class Talk(Base):
    __tablename__ ='talks'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    duration = Column(String, nullable=True)
    talk_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)
    conference_id = Column(Integer, ForeignKey('conferences.id'))
    speakers = relationship("Speaker")
    participants = relationship("Participant")

