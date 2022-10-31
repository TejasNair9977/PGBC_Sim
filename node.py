import os
import time
import glob
from blockchain import Blockchain
from MyOwnPeer2PeerNode import MyOwnPeer2PeerNode
bc = Blockchain()

node_1 = MyOwnPeer2PeerNode("127.0.0.1", 8001, 1)
node_2 = MyOwnPeer2PeerNode("127.0.0.1", 8002, 2)
node_3 = MyOwnPeer2PeerNode("127.0.0.1", 8003, 3)

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
list_of_files = glob.glob('C:/Program Files/PostgreSQL/14/data/log/*')
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
            block = bc.process_block(item, "transaction")
            bc.add_block(block)
            bc.get_block(i)
            i+=1
    else:
        print('file has not been changed!')

    time.sleep(2)
    