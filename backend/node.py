import os
import time
import glob
from api.blockchain import Blockchain
from api.p2pnode import p2pnode
bc = Blockchain()

node_1 = p2pnode("127.0.0.1", 8001, 1)
node_2 = p2pnode("127.0.0.1", 8002, 2)
node_3 = p2pnode("127.0.0.1", 8003, 3)

time.sleep(1)

node_1.start()
node_2.start()
node_3.start()

time.sleep(1)

debug = False
node_1.debug = debug
node_2.debug = debug
node_3.debug = debug


node_1.connect_with_node('127.0.0.1', 8002)
node_2.connect_with_node('127.0.0.1', 8003)
node_3.connect_with_node('127.0.0.1', 8001)

time.sleep(2)
list_of_files = glob.glob('C:/Program Files/PostgreSQL/*/data/log/*')
sample = max(list_of_files, key=os.path.getctime)
logsize=os.path.getsize(sample)
while True:
    i=0
    if logsize!=os.path.getsize(sample):
        print('file has been changed!')
        with open(sample, 'r') as fp:
            fp.seek(logsize)
            x = fp.readlines()
        logsize=os.path.getsize(sample)
        stripped = [item.strip() for item in x]
        for item in stripped:
            node_1.send_to_nodes(item)
            block = bc.create_block(item)
            print(bc.print_previous_block())
            i+=1
    else:
        print('file has not been changed!')
        print(bc.return_last_five(bc.chain))
    
    print(bc.chain_valid(bc.chain)) 
    time.sleep(2)
    