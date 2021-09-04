from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column

from db.database import Base

class Profile(Base):
    __tablename__ ='profiles'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email= Column(String, nullable=True)


class Participant(Base):
    __tablename__ ='participants'
    id = Column(Integer, primary_key=True)
    profile_id = Column(Integer, ForeignKey('profiles.id'))
    talk_id = Column(Integer, ForeignKey('talks.id'))
    conference_id = Column(Integer, ForeignKey('conferences.id'))

class Speaker(Base):
    __tablename__ ='speakers'
    id = Column(Integer, primary_key=True)
    profile_id = Column(Integer, ForeignKey('profiles.id'))
    talk_id = Column(Integer, ForeignKey('talks.id'))
    conference_id = Column(Integer, ForeignKey('conferences.id'))
