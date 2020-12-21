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

# instantiate contract
abi = json.loads(os.environ.get('abi'))
address = Web3.toChecksumAddress(os.environ.get('address'))

smart_contract = client.eth.contract(address=address,abi=abi)
print(smart_contract.functions.greet().call())
# send data to contract
tx_hash = smart_contract.functions.setGreeting('Hello world from Solidity and Ganache').transact()
# wait for transaction to be minedd and get receipt
Web3.eth.waitForTransactionReceipt(tx_hash)
print(f'New updated greeting {smart_contract.functions.greet().call()}')
