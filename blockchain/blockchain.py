#!/bin/python3

import hashlib
import datetime
import random

class Block:
  def __init__(self, idx, txn_amt, prev_hash):
    self.index = idx
    self.txn_date = datetime.datetime.now()
    self.txn_amount = txn_amt
    self.previous_hash = prev_hash
    self.hash = self.generate_hash()
    
  def generate_hash(self):
    key = hashlib.sha256()
    key.update(str(self.index).encode('utf-8'))
    key.update(str(self.txn_date).encode('utf-8'))
    key.update(str(self.txn_amount).encode('utf-8'))
    key.update(str(self.previous_hash).encode('utf-8'))
    
    return key.hexdigest()
    
  def __str__(self):
    return str(self.index) + " : " + str(self.txn_date) + " : " + str(self.txn_amount) + " : " + self.hash
    
  def __repr__(self):
    return "Block <" + self.__str__ + ">"
    
    
class Chain:
  def genesis_block():
    return Block(0,0,"Genesis")

  def __init__(self):
    self.blocks = [Chain.genesis_block()]
        
  def add_block(self, txn_amt):
    self.blocks.append(Block(len(self.blocks), txn_amt, self.blocks[len(self.blocks)-1].hash))
    
  def print_chain(self):
    for c in self.blocks:
      print(c)
      
  def validate_chain(self, verbose=True):
    valid=True
    
    for i in range(1,len(self.blocks)):
      c = self.blocks[i]
      p = self.blocks[i-1]
      
      if c.previous_hash != p.hash:
        valid = False
        if verbose:
          print("** INVALID BLOCK ** : " + str(c))
      if c.hash != c.generate_hash():
        valid = False
        print("** INVALID BLOCK ** : " + str(c))
      if c.index != i:
        valid = False
        print("** INVALID BLOCK ** : At sequence " + str(i))
      if c.txn_date < p.txn_date:
        valid = False
        print("** INVALID TIMESTAMP ** : At sequence " + str(i))
        
    return valid
    
  def chain_length(self):
    return len(self.blocks)-1

c = Chain()
n_blocks = 500

for i in range(n_blocks):
  c.add_block(random.randint(0,1000))

print("Created a chain of " + str(c.chain_length()) + " blocks.")

c.print_chain()
# c.blocks[random.randint(1,c.chain_length())].txn_amount = 9999
v=c.validate_chain()
print("\nChain Valid : " + str(v))


