from web3 import Web3
import os
infura_url = os.environ.get('infura_url')
client = Web3(Web3.HTTPProvider(infura_url)) # connect to the ethereum blockchain
print(client.isConnected()) # check connection