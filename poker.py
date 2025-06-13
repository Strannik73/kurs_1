import pandas as pd

# создаем  класс
class poker_t_1:
    def __init__ (self, filename_1):
        self.df = pd.read_csv(filename_1)
    
    def __neg__(self):
        return self.df.drop_duplicates()
    
    def sravn_e(self):
        for i in range(10):
            df_te = self.df[self.df['Poker Hand'] == i]
            df_te.to_csv(f'df_test_{i}.csv', index=False )
    
    def __del__(self):
        print('удаление poker_t_1')
        
# наследуем созданный класс
class poker_t_2(poker_t_1):
    def __init__(self, filename_2):
        super().__init__(filename_2)
    

    def sravn_r(self):
        for i in range(10):
            df_tr = self.df[self.df['Poker Hand'] == i]
            df_tr.to_csv(f'df_train_{i}.csv', index=False)
            
    def __del__(self):
        print('удаление poker_t_2')
        
# main
def main():
    poker_1 = poker_t_1('pok.te.csv')
    poker_2 = poker_t_2('pok.tr.csv')
    poker_1.sravn_e()
    poker_2.sravn_r()
    
if __name__ == '__main__':
    main()
