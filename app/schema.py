from pydantic import BaseModel
from uuid import UUID

class Mockdata(BaseModel):
    name: str = None
    city: str = None
    
class Payload(Mockdata):
    id: int
    
    class Config:
        orm_mode = True