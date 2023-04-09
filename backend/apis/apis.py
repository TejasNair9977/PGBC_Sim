# this will define the APIs
import os
import glob
from apis.blockchain import Blockchain
import requests

peers = []
bc = Blockchain()

def initiate():
    global bc
    peers.append("26.154.77.106")
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
        response = requests.post("http://"+ip+":8000/remotechange", block)
        responses.append(response)
    print(bc.print_previous_block())
    return {"new block":block}

def makechange(block):
    bc.chain.append(block)
    return