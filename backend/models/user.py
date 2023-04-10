from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    public_key: str
    private_key: str
    ip_address: str
