from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Change(BaseModel):
    timestamp:datetime
    user:Optional[str] = None
    dbname:Optional[str] = None
    pid:int
    remote_host:Optional[str] = None
    remote_port:Optional[int] = None    
    session_id:str
    line_num:int
    ps:Optional[str] = None
    session_start:datetime
    vxid:Optional[str] = None
    txid:int
    error_severity:str
    message:str
    application_name:Optional[str] = None
    backend_type:str
    query_id:int
