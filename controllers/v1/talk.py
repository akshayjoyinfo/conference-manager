from typing import Any, List

import logging
import sys
from fastapi import APIRouter, Depends, HTTPException
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
