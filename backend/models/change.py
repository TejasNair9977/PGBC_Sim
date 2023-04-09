from pydantic import BaseModel
from datetime import datetime

class Change(BaseModel):
    timestamp:datetime
    user:str
    dbname:str
    pid:int
    remote_host:str
    remote_port:int
    session_id:str
    line_num:int
    ps:str
    session_start:datetime
    vxid:str
    txid:int
    error_severity:str
    message:str
    application_name:str
    backend_type:str
    query_id:int
