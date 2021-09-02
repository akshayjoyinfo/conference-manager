from typing import Any, List

import logging
import sys
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas.conference import CreateConferenceCommand, ConferenceResponse, ConferenceResponse
from db.database import get_db
from models.conference import Conference

logging.config.fileConfig('logger.conf', disable_existing_loggers=False)

logger = logging.getLogger(__name__)


conference_router = APIRouter()




@conference_router.post('/')
def create_conference(details: CreateConferenceCommand, db: Session = Depends(get_db)):
    to_create = Conference(
        title = details.title,
        description = details.description,
        start_date = details.start_date,
        end_date = details.end_date
    )
    db.add(to_create)
    db.commit()
   
    return {
        "success": True,
        "created_id": to_create.id
    }

@conference_router.get("/", response_model=List[ConferenceResponse])
def get_conferences( db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100):
    conferences = db.query(Conference).offset(skip).limit(limit).all()
    return conferences