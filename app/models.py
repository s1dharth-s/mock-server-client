from sqlalchemy.types import JSON, Integer, String
from sqlalchemy import Column

from .database import Base

class Payload(Base):
    __tablename__ = "payloads"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String)
    