from typing import Any, List

import logging
import sys
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from schemas.conference import CreateConferenceCommand, ConferenceResponse, ConferenceResponse, UpdateConferenceCommand
from db.database import get_db
from models.conference import Conference
from models.talk import Talk

logging.config.fileConfig('logger.conf', disable_existing_loggers=False)

logger = logging.getLogger(__name__)


conference_router = APIRouter()




@conference_router.post('')
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

@conference_router.get("", response_model=List[ConferenceResponse])
def get_conferences( db: Session = Depends(get_db),
    skip: int = Query(0),
    limit: int = Query(10)):
    conferences = db.query(Conference).order_by(Conference.id.desc()).offset(skip).limit(limit).all()
    return conferences

@conference_router.get("/{id}", response_model=ConferenceResponse)
def get_conference_detail( id: int, db: Session = Depends(get_db)):
    conference = db.query(Conference).get(id)

    if not conference:
        raise HTTPException(status_code=404, detail="Invalid Confernece not found")
    
    return conference



@conference_router.put("/{id}", response_model=ConferenceResponse)
def update_conference( id: int, details: UpdateConferenceCommand, db: Session = Depends(get_db)):

    conf = db.query(Conference).get(id)
    if not conf:
        raise HTTPException(status_code=404, detail="Invalid Confernece not found")

    to_update = Conference(
        title = details.title,
        description = details.description,
        start_date = details.start_date,
        end_date = details.end_date
    )

    conf.title = to_update.title
    conf.description = to_update.description
    conf.start_date = to_update.start_date
    conf.end_date = to_update.end_date

    db.commit()
    db.refresh(conf)
   
    return conf
