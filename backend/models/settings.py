from pydantic import BaseModel
from typing import Optional

class Settings(BaseModel):
    authjwt_algorithm: str = "RS512"
    authjwt_public_key: Optional[str] = None
    authjwt_private_key: Optional[str] = None
    ip_address: Optional[str]
