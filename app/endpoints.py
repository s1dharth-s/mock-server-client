from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException

from .import schema, models
from .database import SessionLocal, engine, get_db

 
router = APIRouter(prefix="/data",
                   tags=["Data"],
                   responses={404: {"description": "Not Found!"}})


@router.put("/", response_model = schema.Payload | List[schema.Payload])
def store_payload(id: int, payload: schema.Mockdata, db = Depends(get_db)):
    """Update stored JSON payload by ID."""
    db_data = db.query(models.Payload).filter(models.Payload.id == id).first()
    if not db_data:
        # I assume that since it is PUT method, we are updating already existing data
        # So if an entry by the id is not found, return a 404 error
        raise HTTPException(404, detail=f"An entry with ID:{id} could not be found.")
    
    # Only update set values
    update_data = payload.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_data, field, value)
        
    db.commit()
    db.refresh(db_data)
    return db_data
    

@router.get("/", response_model= schema.Payload | List[schema.Payload])
def get_payload(id: int = None, db = Depends(get_db)):
    "Fetch stored data by the id. If no ID is provided, return all values"
    if not id:
        return db.query(models.Payload).all()
    
    return db.query(models.Payload).filter(models.Payload.id == id).first()
    