import requests
import pandas as pd
from utils.python_utils import str_to_dict
from utils.yaml_utils import *
from utils.colors import *

URL_BASE = yaml_to_dict('ressources/path.yaml')


class Coin:
    def __init__(self, coin:str, hours=4):
        self.coin = coin
        self.hours = hours

    def get_price(self):
        currency = 'USDT'
        price = requests.get(f'{URL_BASE["path"]["base_url"]}/ticker/price?symbol={self.coin.upper()}{currency}')
        dic = str_to_dict(price.text)
        print(f"{bcolors.BOLD}{self.coin}{bcolors.ENDC} ACTUAL PRICE :{bcolors.YELLOW} {dic['price']} {currency}")
        return price

    def get_df(self, period=0, daily=False):
        if daily:
            r = requests.get(f'{URL_BASE["path"]["base_url"]}/klines?symbol=BTCUSDT&interval={self.hours}d')
        else:
            if self.coin == 'BTC':
                r = requests.get(f'{URL_BASE["path"]["base_url"]}/klines?symbol=BTCUSDT&interval={self.hours}h')
            else:
                r = requests.get(f'{URL_BASE["path"]["base_url"]}/klines?symbol={self.coin.upper()}USDT&interval={self.hours}h')
        json_response = r.json()
        df = pd.DataFrame.from_dict(json_response)
        headers = ['OPEN_TIME', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME', 'CLOSE_TIME', 'QUOTE_ASSET_VOLUME', 'NB_OF_TRADES', 'TAKER_BUY_BASE_ASSET_VOLUME', 'TAKER_BUY_QUOTE_ASSET_VOLUME', 'IGNORE']
        df.set_axis(headers, axis=1, inplace=True)
        return df[500-period:]

if __name__ == '__main__':
    info = Coin('BTC')
    info.get_price()
    print(info.get_df().head())