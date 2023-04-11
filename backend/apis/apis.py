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

load_dotenv()
shared_secret = os.getenv("SECRETPASS")
peers = ["26.225.70.86"]#TODO 
bc = Blockchain()

larger_activity=[0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0]

activity = [0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0]

def passtime():
    activity.pop(0)
    activity.append(0)

def hourtime():
    larger_activity.pop(0)
    larger_activity.append(sum(activity))

scheduler = BackgroundScheduler()
scheduler.add_job(passtime, 'interval', minutes=1)
scheduler.add_job(hourtime, 'interval', minutes=60)
scheduler.start()

def addact():
    activity[-1]+=1

def initiate():
    activity[-1]+=1
    global bc
    return {"Connection status":"Successful"}

def change():
    activity[-1]+=1
    global bc
    list_of_files = glob.glob('C:/Program Files/PostgreSQL/*/data/log/*')#TODO "Remove it"
    sample = max(list_of_files, key=os.path.getctime)
    with open(sample, "rb") as file:
        try:
            file.seek(-2, os.SEEK_END)
            while file.read(1) != b'\n':
                file.seek(-2, os.SEEK_CUR)
        except OSError:
            file.seek(0)
        last_line = file.readline().decode()
    print(last_line)
    block = bc.create_block(last_line)
    responses=  []
    for ip in peers:
        print("http://"+ip+":8000/remotechange")
        response = requests.post("http://"+ip+":8000/remotechange", block)
        responses.append(response)
    print(bc.print_previous_block())
    return {"new block":block}

async def connect_to_db():
    activity[-1]+=1
    conn = await asyncpg.connect(
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        host=os.getenv("HOST"),
        port=os.getenv("PORT"),
        database=os.getenv("DB")
    )
    return conn

def ret_db_name():
    activity[-1]+=1
    return os.getenv("DB")

def generate_key_pair():
    activity[-1]+=1
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


async def makechange(block):
    activity[-1]+=1
    conn = await connect_to_db()
    print(type(block))
    bc.chain.append(block)
    response = await conn.fetch(block.data.message[11:])
    return {'new_block':response}

async def query_blocks():
    activity[-1]+=1
    last_five = bc.return_last_five()
    return {"last_five_blocks": last_five}

async def return_peers():
    activity[-1]+=1
    return {"peers":peers}

async def get_total_traffic():
    return {"hourly":larger_activity, "minute":activity}