# this will define the APIs
import os
import glob
from apis.blockchain import Blockchain
from apis.p2pnode import p2pnode
nodelist = [p2pnode("127.0.0.1", 8001, 1)]
bc = Blockchain()

def initiate():
    global bc
    global nodelist
    node_1=nodelist[0]
    node_2 = p2pnode("127.0.0.1", 8002, 2)
    nodelist.append(node_2)
    node_3 = p2pnode("127.0.0.1", 8003, 3)
    nodelist.append(node_3)
    try:
        node_1.start()
        node_2.start()
        node_3.start()
    except:
        print("Nodes already started!")

    debug = False
    node_1.debug = debug
    node_2.debug = debug
    node_3.debug = debug

    node_1.connect_with_node('127.0.0.1', 8002)
    node_2.connect_with_node('127.0.0.1', 8003)
    node_3.connect_with_node('127.0.0.1', 8001)
    return {"Connection status":"Successful"}

def change():
    global nodelist
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
    nodelist[0].send_to_nodes(last_line)
    block = bc.create_block(last_line)
    print(bc.print_previous_block())
    return {"new block":block}