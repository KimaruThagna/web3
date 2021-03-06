from web3 import Web3
from dotenv import load_dotenv
import os
load_dotenv('.env')
ganache_url = os.environ.get('ganache_url')

account_1 = os.environ.get('account_1')
account_2 = os.environ.get('account_2')

private_key_1 = os.environ.get('private_key_1')


client = Web3(Web3.HTTPProvider(ganache_url)) # connect to the ethereum blockchain
print(client.isConnected()) # check connection
# latest block
print(client.eth.blockNumber)

#build transaction
transaction = {
    'nonce':client.eth.getTransactionCount(account_1), #helps prevent sending same transactions twice by sender
    'to':account_2,
    'value':Web3.toWei(1,'ether'), # sending 1 ether as Wei amount
    'gas': 100000, # gas limit. Max units of gas we are willing to pay for the transaction to be mined
    'gasPrice': Web3.toWei('50','gwei')
}

#sign transaction with private key of sender
signed_transaction = client.eth.account.signTransaction(transaction,private_key_1)

#send transaction
transaction_hash = client.eth.sendRawTransaction(signed_transaction.rawTransaction)
print(transaction_hash)
# make human readable hash
print(Web3.toHex(transaction_hash))