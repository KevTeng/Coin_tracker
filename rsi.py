from functools import reduce
from utils.yaml_utils import *
import requests
import ast
import pandas as pd
import json
import pandas as md
import numpy as np
from price import *
from utils.colors import *

import time

def get_rsi(coin: str, hours = 4): #4 hours by default
    average_gain = 0
    average_loss = 0
    rs = 0
    # print('debug1')
    gain = []
    loss = []
    df = get_df(coin, hours)
    for i in range(len(df)): #14 periods
        # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(df.iloc[i]['OPEN_TIME']) / 1000)))
        if ((float(df.iloc[i]['CLOSE']) - float(df.iloc[i]['OPEN'])) > 0.0):
            gain.append((float(df.iloc[i]['CLOSE']) - float(df.iloc[i]['OPEN'])))
        else:
            loss.append(abs((float(df.iloc[i]['CLOSE']) - float(df.iloc[i]['OPEN']))))
    sum_av_gain = sum(gain) / 14
    sum_av_loss = sum(loss) / 14
    rs = sum_av_gain / sum_av_loss
    rsi = 100 - (100 / (1 + rs))
    if rsi < 30:
        print(f"{bcolors.RED} RSI on OVERSOLD = {rsi} {bcolors.ENDC}")
    elif rsi <= 50:
        print(f"{bcolors.RED} RSI  = {rsi} {bcolors.ENDC}")
    elif rsi <= 70:
        print(f"{bcolors.OKGREEN} RSI = {rsi} {bcolors.ENDC}")
    else:
        print(f"{bcolors.OKGREEN} RSI on OVERBUY = {rsi} {bcolors.ENDC}")
    return rsi

if __name__ == '__main__':
    get_rsi('BTC')
    pass