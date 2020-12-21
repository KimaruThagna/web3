from web3 import Web3
from dotenv import load_dotenv
import os
load_dotenv('.env')
ganache_url = os.environ.get('ganache_url')
client = Web3(Web3.HTTPProvider(ganache_url)) # connect to the ethereum blockchain
print(client.isConnected()) # check connection
# latest block
print(client.eth.blockNumber)

