from web3 import Web3
import os
infura_url = os.environ.get('infura_url')
client = Web3(Web3.HTTPProvider(infura_url)) # connect to the ethereum blockchain
print(client.isConnected()) # check connection
# latest block
latest = client.eth.blockNumber
print(latest)
##3 get block details
print(client.eth.getBlock(latest))
# details of the genesis block
print(client.eth.getBlock(0))
block_hash = os.environ.get('block_hash')
transaction = client.eth.getTransactionByBlock(block_hash,1) # transaction at index 1
print(transaction)
