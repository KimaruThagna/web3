from web3 import Web3
import os
infura_url = os.environ.get('infura_url')
client = Web3(Web3.HTTPProvider(infura_url)) # connect to the ethereum blockchain
print(client.isConnected()) # check connection
#create account
account = client.eth.account.create()
print(account)
# the private key is very sensitive and should be stored in encrypted format
passphrase = 'my passphrase'
keystore = account.encrypt(passphrase)