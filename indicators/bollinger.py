from indicators.price import *


def get_bollinger(coin: str, hours: int = 4):
    df = get_df(coin,period=20, hours=hours)
    df['20MA'] = df['CLOSE'].rolling(window=20).mean()
    df['20_std_dev'] = df['CLOSE'].rolling(window=20).std()
    df['UPPER'] = df['20MA'] + 2*df['20_std_dev']
    df['LOWER'] = df['20MA'] - 2*df['20_std_dev']
    print(f"LOWER BAND = {df.iloc[-1]['LOWER']}")
    print(f"MIDDLE BAND = {df.iloc[-1]['20MA']}")
    print(f"UPPER BAND = {df.iloc[-1]['UPPER']}")
    return df.iloc[-1]['LOWER'], df.iloc[-1]['20MA'], df.iloc[-1]['UPPER']

if __name__ == '__main__':
    a = get_bollinger('BTC')
    pass
