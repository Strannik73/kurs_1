import pandas as pd
import time

# создаем  класс
class poker_t_1:
    def __init__ (self, filename_1):
        self.df = pd.read_csv(filename_1)
    
    def __neg__(self):
        return self.df.drop_duplicates()
    
    def sravn_e(self):
        start = time.time()
        for i in range(10):
            df_te = self.df[self.df['Poker Hand'] == i]
            df_te.to_csv(f'df_test_{i}.csv', index=False )
        end = time.time()
        print(f' время на выполнение "sravn_e": {end - start:.4f} секунды ')
        
    def __del__(self):
        print('удаление poker_t_1')
        
# наследуем созданный класс
class poker_t_2(poker_t_1):
    def __init__(self, filename_2):
        super().__init__(filename_2)
    

    def sravn_r(self):
        start = time.time()
        for i in range(10):
            df_tr = self.df[self.df['Poker Hand'] == i]
            df_tr.to_csv(f'df_train_{i}.csv', index=False)
        end =time.time()
        print(f' время на выполнение "sravn_e": {end - start:.4f} секунды ')
        
    def __del__(self):
        print('удаление poker_t_2')
        
        
# main
def main():
    class_start = time.time()
    poker_1 = poker_t_1('pok.te.csv')
    poker_2 = poker_t_2('pok.tr.csv')
    poker_1.sravn_e()
    poker_2.sravn_r()
    class_end = time.time()
    print(f' Общее время выполнения : {class_end - class_start}')
    
if __name__ == '__main__':
    main()
