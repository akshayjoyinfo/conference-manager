from typing import Any, List

import logging
import sys
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from enum import Enum

from schemas.talk import CreateTalkCommand, TalkResponse, UpdtaeTalkCommand
from schemas.profile import CreateProfileCommand
from db.database import get_db
from models.talk import Talk
from models.profile import Profile, Participant, Speaker
from models.conference import Conference

logging.config.fileConfig('logger.conf', disable_existing_loggers=False)

logger = logging.getLogger(__name__)


talk_manager_router = APIRouter()



class TalkUserType(str, Enum):
    participant = "participant"
    speaker = "speaker"


@talk_manager_router.post('/{confid}/talks/{talkid}/{talk_user}')
def add_talk_participants_or_speakers(confid: int, talkid: int, talk_user: TalkUserType, userDetails: CreateProfileCommand, db: Session = Depends(get_db)):
    """
    Add Participants/Speakers to talk
    """
    conf = db.query(Conference).get(confid)
    resource_id  = None

    if not conf:
        raise HTTPException(status_code=404, detail="Invalid Confernece reference not found")

    talk = db.query(Talk).get(talkid)
    if not talk:
        raise HTTPException(status_code=404, detail="Invalid Talk reference not found")

    to_create = Profile(
        username = userDetails.username,
        email = userDetails.email
    )

    # chcking that incoming request user as already exists in database or not
    #  if exists take taht profile_id tag ito and again if the participant has already been registered just 
    # re update the entry we could have written 4xx saying that reques can not be processed its already exists

    check_profile = db.query(Profile).filter(Profile.email==to_create.email).first()
    
    if not check_profile:
        db.add(to_create)
        db.commit()

        if talk_user==TalkUserType.participant :
            to_create_participant = Participant(
                profile_id= to_create.id,
                talk_id= talkid ,
                conference_id=confid
            )
            db.add(to_create_participant)
            db.commit()
            resource_id = to_create_participant.id
        else :
            to_create_speaker = Speaker(
                profile_id= to_create.id,
                talk_id= talkid ,
                conference_id=confid
            )
            db.add(to_create_speaker)
            db.commit()
            resource_id = to_create_speaker.id
    else :
        if talk_user==TalkUserType.participant :
            check_participant = db.query(Participant).filter(Participant.profile_id==check_profile.id, Speaker.talk_id == talkid).first()
            if not check_participant :
                to_create_participant = Participant(
                    profile_id= check_profile.id,
                    talk_id= talkid ,
                    conference_id=confid
                )
                db.add(to_create_participant)
                db.commit()
                resource_id = to_create_participant.id
        else:
            check_speaker = db.query(Speaker).filter(Speaker.profile_id==check_profile.id, Speaker.talk_id == talkid ).first()
            if not check_speaker :
                to_create_speaker = Speaker(
                    profile_id= check_profile.id,
                    talk_id= talkid ,
                    conference_id=confid
                )
                db.add(to_create_speaker)
                db.commit()
                resource_id = to_create_speaker.id

    return {
        "success": True,
        "created_id": resource_id,
        "talk_user_type": talk_user
    }


@talk_manager_router.delete('/{confid}/talks/{talkid}/{talk_user}/{booking_id}')
def remove_talk_participants_or_speakers(confid: int, talkid: int, talk_user: TalkUserType, booking_id: int, db: Session = Depends(get_db)):
    """
    Remove Participants/Speakers to talk
    """

    conf = db.query(Conference).get(confid)
    
    if not conf:
        raise HTTPException(status_code=404, detail="Invalid Confernece reference not found")

    talk = db.query(Talk).get(talkid)

    if not talk:
        raise HTTPException(status_code=404, detail="Invalid Talk reference not found")
    
    if talk_user == TalkUserType.participant :
        to_remove_particpant = db.query(Participant).filter(Participant.id==booking_id, Participant.talk_id == talkid ).first()
        if not to_remove_particpant :
             raise HTTPException(status_code=404, detail="Invalid Booking ID passed")
        db.delete(to_remove_particpant)
        db.commit()
    else:
        to_remove_speaker = db.query(Speaker).filter(Speaker.id==booking_id, Speaker.talk_id == talkid ).first()
        if not to_remove_speaker :
             raise HTTPException(status_code=404, detail="Invalid Booking ID passed")
        db.delete(to_remove_speaker)
        db.commit()

    return {
        "success": True
    }
