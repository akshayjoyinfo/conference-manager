from typing import Any, List

import logging
import sys
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from schemas.talk import CreateTalkCommand, TalkResponse, UpdtaeTalkCommand
from db.database import get_db
from models.talk import Talk
from models.conference import Conference

logging.config.fileConfig('logger.conf', disable_existing_loggers=False)

logger = logging.getLogger(__name__)


talk_router = APIRouter()




@talk_router.post('/{confid}/talks')
def create_talk(confid: int, details: CreateTalkCommand, db: Session = Depends(get_db)):
    
    conf = db.query(Conference).get(confid)
    if not conf:
        raise HTTPException(status_code=404, detail="Invalid Confernece reference not found")

    to_create = Talk(
        title = details.title,
        description = details.description,
        talk_date = details.talk_date,
        duration = details.duration,
        conference_id=confid
    )
    db.add(to_create)
    db.commit()

    return {
        "success": True,
        "created_id": to_create.id
    }

@talk_router.get('/{confid}/talks', response_model=List[TalkResponse])
def get_talks( confid: int,
    db: Session = Depends(get_db),
    skip: int = Query(0),
    limit: int = Query(10)):

    conf = db.query(Conference).get(confid)
    if not conf:
        raise HTTPException(status_code=404, detail="Invalid Confernece reference not found")

    talks = db.query(Talk).filter(Talk.conference_id==confid).offset(skip).limit(limit).all()
    return talks



@talk_router.put("/{id}/talks", response_model=TalkResponse)
def update_talk( id: int, details: UpdtaeTalkCommand, db: Session = Depends(get_db)):

    talk = db.query(Talk).get(id)
    if not talk:
        raise HTTPException(status_code=404, detail="Invalid talk not found")

    to_update = Talk(
        title = details.title,
        description = details.description,
        talk_date = details.talk_date,
        duration = details.duration
    )

    talk.title = to_update.title
    talk.description = to_update.description
    talk.talk_date = to_update.talk_date
    talk.duration = to_update.duration

    db.commit()
    db.refresh(talk)
   
    return talk
