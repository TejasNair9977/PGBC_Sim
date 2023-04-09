import asyncpg
from fastapi.middleware.cors import CORSMiddleware
from fastapi.params import Body
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from fastapi_another_jwt_auth import AuthJWT
from fastapi_another_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel
from typing import Optional
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


app = FastAPI()

class User(BaseModel):
    public_key: str
    private_key: str
    ip_address: str

class Settings(BaseModel):
    authjwt_algorithm: str = "RS512"
    authjwt_public_key: Optional[str] = None
    authjwt_private_key: Optional[str] = None
    ip_address: Optional[str]

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserCredentials(BaseModel):
    public_key: str
    private_key: str

async def connect_to_db():
    conn = await asyncpg.connect(
        user="postgres",
        password="1234",
        database="test",
        host="localhost"
    )
    return conn

@app.get("/employees")# not needed
async def get_employees():
    conn = await connect_to_db()
    rows = await conn.fetch("SELECT * FROM employee")
    await conn.close()
    return {"employees": rows}
@AuthJWT.load_config
def get_config():
    return Settings()

@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ).decode('utf-8')
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode('utf-8')
    return private_pem, public_pem

@app.post('/login')
def login(login_schema: User, Authorize: AuthJWT = Depends()):
    if login_schema.ip_address != "127.0.0.1":
        raise HTTPException(status_code=401, detail="Invalid IP address")

    private_key, public_key = generate_key_pair()
    access_token = Authorize.create_access_token(subject=login_schema.public_key, algorithm=Authorize.get_config().authjwt_algorithm, key=private_key)
    refresh_token = Authorize.create_refresh_token(subject=login_schema.public_key, algorithm=Authorize.get_config().authjwt_algorithm, key=private_key)

    return {"access_token": access_token, "refresh_token": refresh_token}


@app.post('/refresh')
def refresh(Authorize: AuthJWT = Depends()):
    Authorize.jwt_refresh_token_required()

    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=current_user)
    return {"access_token": new_access_token}

@app.get('/protected')
def protected(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()
    return {"user": current_user}

@app.get("/last-eight")
async def last_eight():
    private_key, public_key = generate_key_pair()

    public_key_bytes = public_key.encode('utf-8')
    return {"last_eight": public_key_bytes[-8:].decode()}

@app.get("/backends")
async def get_backends(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    conn = await connect_to_db()
    backend_count = await conn.fetchval("SELECT COUNT(*) FROM pg_stat_activity")
    await conn.close()

    return {"backends": backend_count}


@app.get("/xact_committed")
async def get_xact_committed():
    conn = await connect_to_db()
    rows = await conn.fetch("SELECT pg_stat_get_db_xact_commit(datid) FROM pg_database WHERE datname = current_database()")
    await conn.close()
    return {"xact_committed": rows[0][0]}

@app.get("/xact_rolled_back")
async def get_xact_rolled_back():
    conn = await connect_to_db()
    rows = await conn.fetch("SELECT pg_stat_get_db_xact_rollback(datid) FROM pg_database WHERE datname = current_database()")
    await conn.close()
    return {"xact_rolled_back": rows[0][0]}

@app.get("/blocks_read")
async def get_blocks_read():
    conn = await connect_to_db()
    rows = await conn.fetch("SELECT blks_read FROM pg_stat_database WHERE datname = current_database()")
    await conn.close()
    return {"blocks_read": rows[0][0]}

@app.get("/blocks_hit")
async def get_blocks_hit():
    conn = await connect_to_db()
    rows = await conn.fetch("SELECT blks_hit FROM pg_stat_database WHERE datname = current_database()")
    await conn.close()
    return {"blocks_hit": rows[0][0]}

@app.get("/tuples_returned")
async def get_tuples_returned():
    conn = await connect_to_db()
    rows = await conn.fetch("SELECT tup_returned FROM pg_stat_database WHERE datname = current_database()")
    await conn.close()
    return {"tuples_returned": rows[0][0]}

@app.get("/tuples_fetched")
async def get_tuples_fetched():
    conn = await connect_to_db()
    rows = await conn.fetch("SELECT tup_fetched FROM pg_stat_database WHERE datname = current_database()")
    await conn.close()
    return {"tuples_fetched": rows[0][0]}

@app.get('/tuples/inserted')
async def get_inserted_tuples():
    conn = await connect_to_db()
    row = await conn.fetchrow("SELECT n_tup_ins FROM pg_stat_database WHERE datname = current_database()")
    await conn.close()
    return {"tuples_inserted": row['n_tup_ins']}

@app.get('/tuples/updated')
async def get_updated_tuples():
    conn = await connect_to_db()
    row = await conn.fetchrow("SELECT n_tup_upd FROM pg_stat_database WHERE datname = current_database()")
    await conn.close()
    return {"tuples_updated": row['n_tup_upd']}

@app.get('/tuples/deleted')
async def get_deleted_tuples():
    conn = await connect_to_db()
    row = await conn.fetchrow("SELECT n_tup_del FROM pg_stat_database WHERE datname = current_database()")
    await conn.close()
    return {"tuples_deleted": row['n_tup_del']}

@app.get('/size')
async def get_database_size():
    conn = await connect_to_db()
    row = await conn.fetchrow("SELECT pg_database_size(current_database()) AS size")
    await conn.close()
    return {"size": row['size']}
