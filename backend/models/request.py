from pydantic import BaseModel
from datetime import datetime
from models.block import Block

class Request(BaseModel):
    size:int
    block:Block

