from web3 import Web3
from dotenv import load_dotenv
import json,  os
load_dotenv('.env')
# read in smart contract abi as json
abi = json.loads(os.environ.get('abi'))
address = os.environ.get('address')

smart_contract = Web3.eth.contract(address,abi)
