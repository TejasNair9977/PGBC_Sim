from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    password: str
    ip_address: str
    public_key: str
