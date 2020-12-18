from web3 import Web3
from dotenv import load_dotenv
import os
load_dotenv('.env')
ganache_url = os.environ.get('ganache_url')

account_1 = os.environ.get('account_1')
account_2 = os.environ.get('account_2')

private_key_1 = os.environ.get('private_key_1')
private_key_2 = os.environ.get('private_key_2')

client = Web3(Web3.HTTPProvider(ganache_url)) # connect to the ethereum blockchain
print(client.isConnected()) # check connection
# latest block
print(client.eth.blockNumber)

#build transaction


#sign transaction


#send transaction
