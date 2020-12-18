from .connect import client, Web3
from dotenv import load_dotenv
import json,  os
load_dotenv('.env')
# read in smart contract abi as json
abi = json.loads(os.environ.get('abi'))
address = os.environ.get('address')

smart_contract = client.eth.contract(address,abi)
# token supply in Wei
total_token_supply = smart_contract.functions.totalSupply().cal()
print(Web3.fromWei(total_token_supply,'ether')) # in ethers
# contract name
print(smart_contract.functions.name().call())
print(smart_contract.functions.symbol().call())
# find balance of an account
balance = smart_contract.functions.balanceOf(address).call()
print(balance)
# convert balance tfrom Wei to ether
print(Web3.fromWei(balance,'ether'))
