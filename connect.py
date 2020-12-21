from web3 import Web3
infura_url = 'https://mainnet.infura.io/v3/ee3fe0d462ca4294b10ffbf535619190'
client = Web3(Web3.HTTPProvider(infura_url)) # connect to the ethereum blockchain
print(client.isConnected()) # check connection
# latest block
latest = client.eth.blockNumber
print(latest)
##3 get block details
print(client.eth.getBlock(latest))
# details of the genesis block
print(client.eth.getBlock(0))
