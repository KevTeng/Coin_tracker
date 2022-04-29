from indicators.price import *
from utils.colors import *

class RSI:
    def __init__(self, coin: str, hours=4):
        self.hours = hours
        self.coin = coin

    def get(self): #4 hours by default
        average_gain = 0
        average_loss = 0
        rs = 0
        gain = []
        loss = []
        my_coin = Coin(self.coin, self.hours)
        df = my_coin.get_df(period=14)
        for i in range(len(df)): #14 periods
            if ((float(df.iloc[i]['CLOSE']) - float(df.iloc[i]['OPEN'])) > 0.0):
                gain.append((float(df.iloc[i]['CLOSE']) - float(df.iloc[i]['OPEN'])))
            else:
                loss.append(abs((float(df.iloc[i]['CLOSE']) - float(df.iloc[i]['OPEN']))))
        sum_av_gain = sum(gain) / 14
        sum_av_loss = sum(loss) / 14
        rs = sum_av_gain / sum_av_loss
        rsi = 100 - (100 / (1 + rs))
        if rsi < 30:
            print(f"{bcolors.RED}RSI on OVERSOLD = {rsi} {bcolors.ENDC}")
        elif rsi <= 50:
            print(f"{bcolors.RED}RSI  = {rsi} {bcolors.ENDC}")
        elif rsi <= 70:
            print(f"{bcolors.OKGREEN}RSI = {rsi} {bcolors.ENDC}")
        else:
            print(f"{bcolors.OKGREEN}RSI on OVERBUY = {rsi} {bcolors.ENDC}")
        return rsi

    if __name__ == '__main__':
        get_rsi('BTC')
        pass