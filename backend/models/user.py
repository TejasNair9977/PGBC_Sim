from pydantic import BaseModel

class User(BaseModel):
    password: str
    ip_address: str
    public_key: str