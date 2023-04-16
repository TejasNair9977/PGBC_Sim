import datetime
import hashlib
import json

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block({"message": "Genesis Block"})

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:5] == '00000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def create_block(self, data):
        if len(data)>400:
            data = json.loads(data)
        prev_proof = self.print_previous_block()["proof"]
        new_proof=self.proof_of_work(prev_proof)   
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': new_proof,
                 'data': data,
                 'previous_hash': self.hash(self.print_previous_block())}
        self.chain.append(block)
        return block

    def print_previous_block(self):
        try:
            return self.chain[-1]
        except:
            print("Empty Blockchain!")
            return {'proof':0}

    def return_last_five(self,chain):
        try:
            return chain[-5:]
        except:
            return chain[-len(chain):]

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:5] != '00000':
                return False
            previous_block = block
            block_index += 1
        return True