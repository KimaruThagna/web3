from web3 import Web3
from dotenv import load_dotenv
import os, json
load_dotenv('.env')
ganache_url = os.environ.get('ganache_url')
client = Web3(Web3.HTTPProvider(ganache_url)) # connect to the ethereum blockchain
print(client.isConnected()) # check connection
# latest block
print(client.eth.blockNumber)

# instantiate contract
abi = json.loads(os.environ.get('abi'))
address = Web3.toChecksumAddress(os.environ.get('address'))

smart_contract = client.eth.contract(address=address,abi=abi)
print(smart_contract.functions.greet().call())
# send data to contract
tx_hash = smart_contract.functions.setGreeting('Hello world from Solidity and Ganache').transact()
