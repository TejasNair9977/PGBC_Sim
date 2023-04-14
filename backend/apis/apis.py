# this will define the APIs
import os
import glob
from apis.blockchain import Blockchain
import requests
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import asyncpg
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler
import platform
from fastapi import HTTPException

load_dotenv()
shared_secret = os.getenv("SECRETPASS")
peers = []
bc = Blockchain()
keys = [0,0]
def check_pass(pasw):
    global shared_secret
    if pasw == shared_secret:
        return True
    return False

activity = [0 for _ in range(60)]

st_activity = 0
temp=0

def addact():
    global temp
    global st_activity
    try:
        st_activity+=1
    except UnboundLocalError:
        print("Initializing Activity")
        temp=0
        st_activity=0


def minutetime():
    global temp
    global st_activity
    try:
        temp=st_activity
        activity.append(st_activity)
        activity.pop(0)
    except UnboundLocalError:
        print("Please initialize your node by calling the / API")

scheduler = BackgroundScheduler()
scheduler.add_job(minutetime, 'interval', minutes=1)
scheduler.start()

def initiate():
    global keys
    addact()
    keys[0], keys[1] = generate_key_pair()
    return {"Connection status":"Successful"}

def ret_keypair():
    global keys
    addact()
    return {"public_key":keys[0],"private_key":keys[1]}

async def change():
    global bc
    addact()
    if platform.system() == 'Windows':
        list_of_files = glob.glob('C:/Program Files/PostgreSQL/*/data/log/*')
    elif platform.system() == 'Linux':
        list_of_files = glob.glob('/var/log/postgresql/*')
    else:
        raise HTTPException(status_code=401, detail="Unidentified OS")

    sample = max(list_of_files, key=os.path.getctime)
    with open(sample, "rb") as file:
        try:
            file.seek(-2, os.SEEK_END)
            while file.read(1) != b'\n':
                file.seek(-2, os.SEEK_CUR)
        except OSError:
            file.seek(0)
        last_line = file.readline().decode()
    block = bc.create_block(last_line)
    responses=  []
    data = {
        "block":block,
        "size":len(bc.chain)
    }
    for ip in peers:
        response = await requests.post("http://"+ip+":8000/remotechange", json=data)
        responses.append(response)
    return {"new block":block}

async def connect_to_db():
    addact()
    conn = await asyncpg.connect(
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        host=os.getenv("HOST"),
        port=os.getenv("PORT"),
        database=os.getenv("DB")
    )
    return conn

def ret_db_name():
    addact()
    return os.getenv("DB")

def generate_key_pair():
    addact()
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


async def makechange(block, size):
    addact()
    conn = await connect_to_db()
    if size>len(bc.chain):
        bc.chain.append(block)
        if block.data.message[11:17].strip()=="insert":
            response = await conn.execute(block.data.message[11:])
        elif block.data.message[11:17].strip()=="update":
            response = await conn.execute(block.data.message[11:])
        elif block.data.message[11:17].strip()=="delete":
            response = await conn.execute(block.data.message[11:])
    else:
        return {'response':"already have data"}
    return {'new_block':response}

def query_blocks():
    addact()
    last_five = bc.return_last_five(bc.chain)
    return {"last_five_blocks": last_five}

def return_peers():
    addact()
    return {"peers":peers}

def get_total_traffic():
    return {"minute":activity}

def get_dynamic_traffic():
    return {"second":[st_activity,temp]}