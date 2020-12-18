from web3 import Web3
from dotenv import load_dotenv
import os
load_dotenv('.env')
ganache_url = os.environ.get('ganache_url')
