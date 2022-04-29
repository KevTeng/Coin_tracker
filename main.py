from indicators.rsi import *
from indicators.bollinger import *

def main():
    infos = Coin('BTC')
    infos.get_price()
    rsi = RSI('BTC')
    rsi.get()
if __name__ == '__main__':
    main()