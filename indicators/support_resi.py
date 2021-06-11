from indicators.price import *
from utils.colors import *

YAML_LIST_NAME = yaml_to_dict(f'/ressources/coin.yaml')





def get_info(df: md.DataFrame):
    high = reduce(lambda x, y: x if x > y else y, df.HIGH)
    low = reduce(lambda x, y: x if x < y else y, df.HIGH)
    close = df.iloc[len(df)-1].CLOSE
    pivot_point = float(float(high) + float(low) + float(close)) / 3

    f_resi = '{:.15f}'.format((2* pivot_point) - float(low))
    f_support = '{:.15f}'.format((2 * pivot_point) - float(high))

    s_resi = '{:.15f}'.format(pivot_point + (float(high) - float(low)))
    s_support = '{:.15f}'.format(pivot_point - (float(high) + float(low)))

    t_resi = '{:.15f}'.format(float(high) + 2 * (pivot_point - float(low)))
    t_support = '{:.15f}'.format(float(low) -  2 * (float(high) - pivot_point))

    print(f'{bcolors.OKGREEN}FIRST RESISTANCE : {f_resi} \nFIRST SUPPORT : {f_support}{bcolors.ENDC}')
    print(f'{bcolors.OKGREEN}SECOND RESISTANCE : {s_resi} \nSECOND SUPPORT : {s_support}{bcolors.ENDC}')
    print(f'{bcolors.OKGREEN}THIRD RESISTANCE : {t_resi} \nTHIRD SUPPORT : {t_support}{bcolors.ENDC}')
    print('')




if __name__ == '__main__':
    # get_price('LTC')
    # for coin in YAML_LIST_NAME['coin']:
    #     get_info(get_df(coin))
    get_info(get_df('CRV', hours = 4))
    # print(r.text)