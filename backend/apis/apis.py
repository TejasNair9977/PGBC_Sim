# this will define the APIs
import os
import glob
from apis.blockchain import Blockchain
import requests
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import asyncpg

peers = ["26.225.70.86"]
bc = Blockchain()

def initiate():
    global bc
    return {"Connection status":"Successful"}

def change():
    global bc
    list_of_files = glob.glob('C:/Program Files/PostgreSQL/*/data/log/*')
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
    conn = await asyncpg.connect(
        user="postgres",
        password="1234",
        database="test",
        host="localhost"
    )
    return conn


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


def makechange(block):
    bc.chain.append(block)      #to be done later
    return {'new_block':bc.print_previous_block()}
