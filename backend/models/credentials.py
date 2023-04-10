from pydantic import BaseModel
from typing import Optional

class UserCredentials(BaseModel):
    public_key: str
    private_key: str
