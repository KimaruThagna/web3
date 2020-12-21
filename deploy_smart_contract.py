from web3 import Web3
from dotenv import load_dotenv
import os, json
load_dotenv('.env')
ganache_url = os.environ.get('ganache_url')
client = Web3(Web3.HTTPProvider(ganache_url)) # connect to the ethereum blockchain
print(client.isConnected()) # check connection
# latest block
print(client.eth.blockNumber)
# designate first account to be default account
Web3.eth.defaultAccount = Web3.eth.accounts[0]


abi = json.loads(os.environ.get('abi'))
address = Web3.toChecksumAddress(os.environ.get('address'))
contract_byte_code = os.environ.get('byte_code')