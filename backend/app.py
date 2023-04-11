from fastapi import FastAPI, HTTPException, Depends, Request
from apis import apis as api
from models.block import Block
from models.user import User
from models.settings import Settings
from models.block import Block
from fastapi_another_jwt_auth import AuthJWT
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi_another_jwt_auth.exceptions import AuthJWTException
keys={}

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    api.initiate()
    return {"message": "Connection Complete"}

@app.get("/change")
async def root():
    print(api.change())
    return {"message": "There was a change in the database"}

@app.post("/remotechange")
async def root(block:Block):
    response = await api.makechange(block)
    return {"status":response}

@app.post('/login')
def login(login_schema: User, Authorize: AuthJWT = Depends()):
    if login_schema.ip_address != "127.0.0.1":
        raise HTTPException(status_code=401, detail="Invalid IP address")

    private_key, public_key = api.generate_key_pair()
    access_token = Authorize.create_access_token(subject=login_schema.public_key, algorithm=Authorize.get_config().authjwt_algorithm, key=private_key)
    refresh_token = Authorize.create_refresh_token(subject=login_schema.public_key, algorithm=Authorize.get_config().authjwt_algorithm, key=private_key)

    keys["public_key"] = public_key
    keys["private_key"] = private_key

    return {"access_token": access_token, "refresh_token": refresh_token}
@app.get("/employees")# not needed
async def get_employees():
    conn = await api.connect_to_db()
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
async def last_eight(Authorize: AuthJWT = Depends()):
    public_key = Authorize.get_jwt_subject()
    public_key = keys["public_key"]
    public_key_bytes = public_key.encode('utf-8')
    return {"last_eight": public_key_bytes[-8:].decode()}

@app.get("/backends")
async def get_backends(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    conn = await api.connect_to_db()
    backend_count = await conn.fetchval("SELECT COUNT(*) FROM pg_stat_activity;")
    await conn.close()
    return {"backends": backend_count}

@app.get("/xact_committed")
async def get_xact_committed():
    conn = await api.connect_to_db()
    db = api.ret_db_name()
    rows = await conn.fetch("select xact_committed from pg_stat_database where datname=%s;"%db)
    await conn.close()
    return {"xact_committed": rows}

@app.get("/xact_rolled_back")
async def get_xact_rolled_back():
    conn = await api.connect_to_db()
    db = api.ret_db_name()
    rows = await conn.fetch("select xact_rollback from pg_stat_database where datname=%s;"%db)
    await conn.close()
    return {"xact_rolled_back": rows}

@app.get("/blocks_read")
async def get_blocks_read():
    conn = await api.connect_to_db()
    db = api.ret_db_name()
    rows = await conn.fetch("select blks_read from pg_stat_database where datname=%s;"%db)
    await conn.close()
    return {"blocks_read": rows}

@app.get("/blocks_hit")
async def get_blocks_hit():
    conn = await api.connect_to_db()
    db = api.ret_db_name()
    rows = await conn.fetch("select blks_hit from pg_stat_database where datname=%s;"%db)
    await conn.close()
    return {"blocks_hit": rows}

@app.get("/tuples_returned")
async def get_tuples_returned():
    conn = await api.connect_to_db()
    db = api.ret_db_name()
    rows = await conn.fetch("select tup_returned from pg_stat_database where datname=%s;"%db)
    await conn.close()
    return {"tuples_returned": rows}

@app.get("/tuples_fetched")
async def get_tuples_fetched():
    conn = await api.connect_to_db()
    db = api.ret_db_name()
    rows = await conn.fetch("select tup_fetched from pg_stat_database where datname=%s;"%db)
    await conn.close()
    return {"tuples_fetched": rows}

@app.get('/tuples_inserted')
async def get_inserted_tuples():
    conn = await api.connect_to_db()
    db = api.ret_db_name()
    rows = await conn.fetch("select tup_inserted from pg_stat_database where datname=%s;"%db)
    await conn.close()
    return {"tuples_inserted": rows}

@app.get('/tuples_updated')
async def get_updated_tuples():
    conn = await api.connect_to_db()
    db = api.ret_db_name()
    rows = await conn.fetch("select tup_updated from pg_stat_database where datname=%s;"%db)
    await conn.close()
    return {"tuples_updated": rows}

@app.get('/tuples_deleted')
async def get_deleted_tuples():
    conn = await api.connect_to_db()
    db = api.ret_db_name()
    rows = await conn.fetch("select tup_deleted from pg_stat_database where datname=%s;"%db)
    await conn.close()
    return {"tuples_deleted": rows}

@app.get('/size')
async def get_database_size():
    conn = await api.connect_to_db()
    db = api.ret_db_name()
    row = await conn.fetchrow("SELECT pg_database_size(%s) AS size;"%db)
    await conn.close()
    return {"size": row}

@app.get("/query")
async def get_last_five_blocks():
    last_five_blocks = await api.query_blocks()
    return last_five_blocks

@app.get("/get_peers")
async def get_peers():
    peers = await api.peers()
    return peers
