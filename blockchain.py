import json
import hashlib
import sqlite3
from datetime import time, date, datetime
from cryptography import x509,fernet

class Blockchain:

    def __init__(self):
        super(Blockchain, self).__init__()
        self.db = sqlite3.connect('blockchain.db')
        self.init_database()
        
    def init_database(self):
        c = self.db.cursor()
        c.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='blockchain'")
        if ( c.fetchone()[0] != 1 ):
            c.execute("""CREATE TABLE blockchain(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       prev_hash TEXT,
                       type TEXT,
                       timestamp TEXT,
                       data TEXT,
                       nonce TEXT, 
                       hash TEXT)""")

    def check_block(self, block):
        return True
            
    def add_block(self, block):
        if ( self.check_block(block) ):
            c = self.db.cursor()
            c.execute("INSERT INTO blockchain (prev_hash, type, timestamp, data, nonce, hash) VALUES (?, ?, ?, ?, ?, ?)",
                      ( block["prev_hash"],
                        block["type"], 
                        block["timestamp"],
                        json.dumps(block["data"], sort_keys=True),
                        block["nonce"],
                        block["hash"] ))
            self.db.commit()
            return True

        return False

    def get_blockchain_record(self, data):
        header = ("id", "prev_hash", "type", "timestamp", "data", "nonce", "hash")
        
        if ( len(data) != len(header) ):
            print("Blockchain data does not contain " + len(header) + " elements")
            return None

        record = {}
        for i in range(len(header)):
            record[header[i]] = data[i]
            
        return record
        
    def get_block(self, index):
        c = self.db.cursor()
        c.execute("SELECT * FROM blockchain WHERE id=?", (index,))

        data = c.fetchone()
        if ( data != None ):
            return self.get_blockchain_record(data)

        return None
            
    def get_last_block(self):
        c = self.db.cursor()
        for row in c.execute('SELECT * FROM blockchain ORDER BY id DESC LIMIT 1'):
            return self.get_blockchain_record(row)
        return None

    def process_block(self, data, type):
        last_block = self.get_last_block()
        print("LAST:")
        print(last_block)
        timestamp = datetime.now()
        block = {
            "id"       : (last_block["id"] + 1) if last_block != None else 1,
            "prev_hash": last_block["hash"] if last_block != None else 0,
            "type"     : type,
            "timestamp": timestamp.isoformat(),
            "data"     : data,
            "nonce"    : 0
        }
        difficulty = 5
        h = hashlib.sha512()
        h.update( json.dumps(block, sort_keys=True).encode("utf-8") )
        while ( h.hexdigest()[:difficulty] != "0"*difficulty ):
            block["nonce"] = block["nonce"] + 1
            h.update( json.dumps(block, sort_keys=True).encode("utf-8") )

        block["hash"] = h.hexdigest()

        return block
