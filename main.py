from poker import poker_t_1
from poker import poker_t_2

def main():
    poker_1 = poker_t_1('pok.tr.csv')
    poker_2 = poker_t_2('pok.tr.csv')
    poker_1.sravn_e()
    poker_2.sravn_r()

if __name__ == '__main__':
    main()