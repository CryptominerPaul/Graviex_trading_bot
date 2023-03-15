###################################################
# Graviex Exchange Bot Created by Cryptominer8245 #
#       Marker Maker, WashTrade & Info Bot        #
#                Created 2-22-2023                #
###################################################
import hashlib
import hmac
import requests
import time
import ssl
import json
import os
import logging
import random
from datetime import datetime
from termcolor import colored
from dotenv import load_dotenv

os.system('clear')

load_dotenv()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)


access_key = os.getenv("access_key")
secret_key = os.getenv("secret_key")

symbol = os.getenv("symbol")
base = os.getenv("base")

#####################################################################
# making ssl context - verify should be turned off = False
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# ------------------
# Get markets list
# ------------------

#####################################################################
# Gets data for Market Pair
def get_markets():
    try:
        query = f'https://graviex.net:443/webapi/v3/markets/{symbol}{base}'
        r = requests.get(query)
        r.raise_for_status()
        data = r.json()
        formatted_data = f"\033[1;32m{data['attributes']['name']}:\033[0;0m Trading Fee: {data['attributes']['bid']['fee']}"
        print(formatted_data)
        return data
    except requests.exceptions.RequestException as e:
        print('Failed to retrieve markets data:', e)
        return None

if __name__ == '__main__':
    print(colored(" Graviex Exchange Bot Loading", "light_magenta"))
    markets = get_markets()

    time.sleep(1)
#####################################################################
# To get The rest of the working Code you must contact me  
# for Purchasing it - Thank you
