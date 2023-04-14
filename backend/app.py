from fastapi import FastAPI, Depends, Request, Body
from apis import apis as api
from models.settings import Settings
from models.request import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

keys=["0","0"]

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
    print(await api.change())
    return {"message": "There was a change in the database"}

@app.post("/remotechange")
async def root(block:Request):
    json_data = block.json()
    response = await api.makechange(json_data)
    return {"status":response}

@app.post('/login')#login page
def login(common_pass: str):
    global keys
    if api.check_pass(common_pass):
        keys[0], keys[1] = api.ret_keypair()
        print(keys)
        return {"response":"success"}
    return {"response":"failed"}

@app.get("/last-eight")#Nav bar ie profile name
async def last_eight():
    global keys
    public_key = keys[0]
    print(public_key)
    public_key_bytes = public_key.encode('utf-8')
    return {"last_eight": public_key_bytes[-34:-26].decode()}

@app.get("/query")#dashboard query result
def get_last_five_blocks():
    last_five_blocks = api.query_blocks()
    return {"response":last_five_blocks}

#########################Analysis##############################
@app.get("/backends")
async def get_backends():
    conn = await api.connect_to_db()
    backend_count = await conn.fetchval("SELECT COUNT(*) FROM pg_stat_activity;")
    await conn.close()
    return {"backends": backend_count}

@app.get("/xact_committed")
async def get_xact_committed():
    conn = await api.connect_to_db()
    rows = await conn.fetch("select xact_committed from pg_stat_database;")
    await conn.close()
    return {"xact_committed": rows}

@app.get("/xact_rolled_back")
async def get_xact_rolled_back():
    conn = await api.connect_to_db()
    rows = await conn.fetch("select xact_rollback from pg_stat_database;")
    await conn.close()
    return {"xact_rolled_back": rows}

@app.get("/blocks_read")
async def get_blocks_read():
    conn = await api.connect_to_db()
    rows = await conn.fetch("select blks_read from pg_stat_database;")
    await conn.close()
    return {"blocks_read": rows}

@app.get("/blocks_hit")
async def get_blocks_hit():
    conn = await api.connect_to_db()
    rows = await conn.fetch("select blks_hit from pg_stat_database;")
    await conn.close()
    return {"blocks_hit": rows}

@app.get("/tuples_returned")
async def get_tuples_returned():
    conn = await api.connect_to_db()
    rows = await conn.fetch("select tup_returned from pg_stat_database;")
    await conn.close()
    return {"tuples_returned": rows}

@app.get("/tuples_fetched")
async def get_tuples_fetched():
    conn = await api.connect_to_db()
    rows = await conn.fetch("select tup_fetched from pg_stat_database;")
    await conn.close()
    return {"tuples_fetched": rows}

@app.get('/tuples_inserted')
async def get_inserted_tuples():
    conn = await api.connect_to_db()
    rows = await conn.fetch("select tup_inserted from pg_stat_database;")
    await conn.close()
    return {"tuples_inserted": rows}

@app.get('/tuples_updated')
async def get_updated_tuples():
    conn = await api.connect_to_db()
    rows = await conn.fetch("select tup_updated from pg_stat_database;")
    await conn.close()
    return {"tuples_updated": rows}

@app.get('/tuples_deleted')
async def get_deleted_tuples():
    conn = await api.connect_to_db()
    rows = await conn.fetch("select tup_deleted from pg_stat_database;")
    await conn.close()
    return {"tuples_deleted": rows}

##########################################################################
@app.get("/get_peers") 
def get_peers():
    peers = api.peers()
    return {"response":peers}

@app.get("/get_total_traffic")
def get_peers():
    response = api.get_total_traffic()
    return {"response":response}

@app.get("/get_dynamic_traffic")
def get_peers():
    response = api.get_dynamic_traffic()
    return {"response":response}