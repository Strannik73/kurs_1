from poker import poker_t_1
from poker import poker_t_2

def main():
    smop = poker_t_1('pok.tr.csv')
    smop = poker_t_2('pok.tr.csv')
    smop.sravn_e()
    smop.sravn_r()

if __name__ == '__main__':
    main()