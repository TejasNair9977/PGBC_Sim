from pydantic import BaseModel

class UserCredentials(BaseModel):
    public_key: str
    private_key: str
