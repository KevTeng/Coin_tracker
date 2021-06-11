from functools import reduce
from utils.yaml_utils import *
import requests
import ast
import pandas as pd
import json
import pandas as md
import numpy as np
from utils.python_utils import str_to_dict
from utils.colors import *


def get_price(coin:str):
    if coin == 'BTC':
        currency = 'USDT'
        price = requests.get(f'https://api.binance.com/api/v1/ticker/price?symbol={coin.upper()}{currency}')
    else:
        currency = 'USDT'
        price = requests.get(f'https://api.binance.com/api/v1/ticker/price?symbol={coin.upper()}{currency}')
    dic = str_to_dict(price.text)
    print(f"{bcolors.BOLD}{coin}{bcolors.ENDC} ACTUAL PRICE :{bcolors.YELLOW} {dic['price']} {currency}")
    return price

def get_df(coin: str, hours=1, period=14, daily=False):
    if daily:
        r = requests.get(f'https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval={hours}d')
    else:
        if coin == 'BTC':
            r = requests.get(f'https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval={hours}h')
        else:
            r = requests.get(f'https://api.binance.com/api/v3/klines?symbol={coin.upper()}USDT&interval={hours}h')
    aa = r.json()
    a = np.array(aa)
    df = md.DataFrame()
    for i in range(len(a)):
        df = df.append({'OPEN_TIME': a[i][0], 'OPEN': a[i][1], 'HIGH': a[i][2], 'LOW': a[i][3],
                        'CLOSE': a[i][4], 'VOLUME': a[i][5],
                        'CLOSE_TIME': a[i][6], 'QUOTE_ASSET_VOLUME': a[i][7],
                        'NUMBER_OF_TRADES': a[i][8]}, ignore_index=True)

    # print(f"Coin Name : {bcolors.BOLD} {coin}BTC ")
    return df[500-period:]

if __name__ == '__main__':
    # get_df('THETA')
    price = requests.get(f'https://api.binance.com/api/v1/ticker/price?symbol=BTCUSDT')
    pass