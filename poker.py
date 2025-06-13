import pandas as pd

class poker_t_1:
    def __init__(self, data,):
        self.data = data 
        self.df = pd.read_csv('pok.te.csv')
    
    def __neg__(self):
        return self.df.drop_duplicates
    
    def sravn_e(self):

      
        
        i = self.df['Poker Hand'] 
        
        for i in range(10):
            if i == 0:
                self.df.to_csv('df_test_0.csv') 
            elif i == 1:
                self.df.to_csv('df_test_1.csv') 
            elif i == 2:
                self.df.to_csv('df_test_2.csv')
            elif i == 3:
                self.df.to_csv('df_test_3.csv')
            elif i == 4:
                self.df.to_csv('df_test_4.csv')
            elif i == 5:
                self.df.to_csv('df_test_5.csv')
            elif i == 6:
                self.df.to_csv('df_test_6.csv')
            elif i == 7:
                self.df.to_csv('df_test_7.csv')
            elif i == 8:
                self.df.to_csv('df_test_8.csv')
            elif i == 9:
                self.df.to_csv('df_test_9.csv')




        # if self.df['Poker Hand'] == 0:
        #     self.df.to_csv('df_test_0.csv')   

        # elif self.df['Poker Hand'] == 1:
        #     self.df.to_csv('df_test_1.csv')   

        # elif self.df['Poker Hand'] == 2:
        #     self.df.to_csv('df_test_2.csv')   

        # elif self.df['Poker Hand'] == 3:
        #     self.df.to_csv('df_test_3.csv')

        # elif self.df['Poker Hand'] == 4:
        #     self.df.to_csv('df_test_4.csv')   

        # elif self.df['Poker Hand'] == 5:
        #     self.df.to_csv('df_test_5.csv')   

        # elif self.df['Poker Hand'] == 6:
        #     self.df.to_csv('df_test_6.csv')   

        # elif self.df['Poker Hand'] == 7:
        #     self.df.to_csv('df_test_7.csv')   

        # elif self.df['Poker Hand'] == 8:
        #     self.df.to_csv('df_test_8.csv')   

        # elif self.df['Poker Hand'] == 9:
        #     self.df.to_csv('df_test_9.csv')  

        # self.df_te0 = self.df[self.df['Poker Hand'] == 0 ]    
        # self.df_te1 = self.df[self.df['Poker Hand'] == 1 ]
        # self.df_te2 = self.df[self.df['Poker Hand'] == 2 ] 
        # self.df_te3 = self.df[self.df['Poker Hand'] == 3 ]    
        # self.df_te4 = self.df[self.df['Poker Hand'] == 4 ] 
        # self.df_te5 = self.df[self.df['Poker Hand'] == 5 ] 
        # self.df_te6 = self.df[self.df['Poker Hand'] == 6 ]    
        # self.df_te7 = self.df[self.df['Poker Hand'] == 7 ] 
        # self.df_te8 = self.df[self.df['Poker Hand'] == 8 ] 
        # self.df_te9 = self.df[self.df['Poker Hand'] == 9 ]
        
        # self.df_te0.to_csv('df_test_0.csv')
        # self.df_te1.to_csv('df_test_1.csv')
        # self.df_te2.to_csv('df_test_2.csv')
        # self.df_te3.to_csv('df_test_3.csv')
        # self.df_te4.to_csv('df_test_4.csv')
        # self.df_te5.to_csv('df_test_5.csv')
        # self.df_te6.to_csv('df_test_6.csv')
        # self.df_te7.to_csv('df_test_7.csv')
        # self.df_te8.to_csv('df_test_8.csv')
        # self.df_te9.to_csv('df_test_9.csv')
    
    def __del__():
        print('удаление')

class poker_t_2(poker_t_1):
    def __init__(self, data):
        self.data = data 
        self.df = pd.read_csv('pok.tr.csv')
    
    def __neg__(self):
        return self.df.drop_duplicates
    
    def sravn_r(self):
        self.df = poker_t_2('pok.tr.csv')

        self.df = -self.df

        i = self.df['Poker Hand'] 
        for i in (0, 9):

            if i == 0:
                self.df.to_csv('df_train_0.csv') 
            elif i == 1:
                self.df.to_csv('df_train_1.csv') 
            elif i == 2:
                self.df.to_csv('df_train_2.csv')
            elif i == 3:
                self.df.to_csv('df_train_3.csv')
            elif i == 4:
                self.df.to_csv('df_train_4.csv')
            elif i == 5:
                self.df.to_csv('df_train_5.csv')
            elif i == 6:
                self.df.to_csv('df_train_6.csv')
            elif i == 7:
                self.df.to_csv('df_train_7.csv')
            elif i == 8:
                self.df.to_csv('df_train_8.csv')
            elif i == 9:
                self.df.to_csv('df_train_9.csv')


        # if self.df['Poker Hand'] == 0:
        #     self.df.to_csv('df_train_0.csv')   

        # elif self.df['Poker Hand'] == 1:
        #     self.df.to_csv('df_train_1.csv')   

        # elif self.df['Poker Hand'] == 2:
        #     self.df.to_csv('df_train_2.csv')   

        # elif self.df['Poker Hand'] == 3:
        #     self.df.to_csv('df_train_3.csv')

        # elif self.df['Poker Hand'] == 4:
        #     self.df.to_csv('df_train_4.csv')   

        # elif self.df['Poker Hand'] == 5:
        #     self.df.to_csv('df_train_5.csv')   

        # elif self.df['Poker Hand'] == 6:
        #     self.df.to_csv('df_train_6.csv')   

        # elif self.df['Poker Hand'] == 7:
        #     self.df.to_csv('df_train_7.csv')   

        # elif self.df['Poker Hand'] == 8:
        #     self.df.to_csv('df_train_8.csv')   

        # elif self.df['Poker Hand'] == 9:
        #     self.df.to_csv('df_train_9.csv')       

        # self.df_tr1 = self.df[self.df['Poker Hand'] == 1 ]
        # self.df_tr2 = self.df[self.df['Poker Hand'] == 2 ] 
        # self.df_tr3 = self.df[self.df['Poker Hand'] == 3 ]    
        # self.df_tr4 = self.df[self.df['Poker Hand'] == 4 ] 
        # self.df_tr5 = self.df[self.df['Poker Hand'] == 5 ] 
        # self.df_tr6 = self.df[self.df['Poker Hand'] == 6 ]    
        # self.df_tr7 = self.df[self.df['Poker Hand'] == 7 ] 
        # self.df_tr8 = self.df[self.df['Poker Hand'] == 8 ] 
        # self.df_tr9 = self.df[self.df['Poker Hand'] == 9 ]
        
        # self.df_tr0.to_csv('df_train_0.csv')
        # self.df_tr1.to_csv('df_train_1.csv')
        # self.df_tr2.to_csv('df_train_2.csv')
        # self.df_tr3.to_csv('df_train_3.csv')
        # self.df_tr4.to_csv('df_train_4.csv')
        # self.df_tr5.to_csv('df_train_5.csv')
        # self.df_tr6.to_csv('df_train_6.csv')
        # self.df_tr7.to_csv('df_train_7.csv')
        # self.df_tr8.to_csv('df_train_8.csv')
        # self.df_tr9.to_csv('df_train_9.csv')


    
    def __del__():
        print('удаление')
        

def main():
    poker = poker_t_1('pok.te.csv')
    poker = poker_t_2('pok.tr.csv')
    poker.sravn_e()
    poker.sravn_r()
    
if __name__ == '__main__':
    main()
