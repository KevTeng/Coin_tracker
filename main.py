from indicators.rsi import *
from indicators.bollinger import *

def main():
    get_rsi('BTC')
    get_bollinger('BTC')
    get_price('BTC')

if __name__ == '__main__':
    main()