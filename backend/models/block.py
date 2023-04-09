from pydantic import BaseModel
from datetime import datetime
from models.change import Change

class Block(BaseModel):
    index:int
    timestamp: datetime
    proof:int
    data:Change
    previous_hash:str
