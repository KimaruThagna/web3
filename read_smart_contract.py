from .connect import client, Web3
from dotenv import load_dotenv
import json,  os
load_dotenv('.env')
# read in smart contract abi as json
abi = json.loads(os.environ.get('abi'))
address = os.environ.get('address')
account = os.environ.get('account_1')
smart_contract = client.eth.contract(address,abi)
# token supply in Wei
total_token_supply = smart_contract.functions.totalSupply().call()
print(Web3.fromWei(total_token_supply,'ether')) # in ethers
# contract name
print(smart_contract.functions.name().call())
print(smart_contract.functions.symbol().call())
# find balance of an account
balance = smart_contract.functions.balanceOf(account).call()
print(balance)
# convert balance tfrom Wei to ether
print(Web3.fromWei(balance,'ether'))
