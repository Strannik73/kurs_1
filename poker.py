import pandas as pd

class poker_t:
    def __init__(self, data,):
        self.data = data 
        self.df = pd.read_csv('pok.te.csv')
    
    def __neg__(self):
        return self.df.drop_duplicates
    
    def sravn(self):
        self.df = poker_t('pok.te.csv')

        self.df = -self.df
        
        self.df0 = self.df[self.df['Poker Hand'] == 0 ]    
        self.df1 = self.df[self.df['Poker Hand'] == 1 ]
        self.df2 = self.df[self.df['Poker Hand'] == 2 ] 
        self.df3 = self.df[self.df['Poker Hand'] == 3 ]    
        self.df4 = self.df[self.df['Poker Hand'] == 4 ] 
        self.df5 = self.df[self.df['Poker Hand'] == 5 ] 
        self.df6 = self.df[self.df['Poker Hand'] == 6 ]    
        self.df7 = self.df[self.df['Poker Hand'] == 7 ] 
        self.df8 = self.df[self.df['Poker Hand'] == 8 ] 
        self.df9 = self.df[self.df['Poker Hand'] == 9 ]
        
        self.df0.to_csv('df0.csv')
        self.df1.to_csv('df1.csv')
        self.df2.to_csv('df2.csv')
        self.df3.to_csv('df3.csv')
        self.df4.to_csv('df4.csv')
        self.df5.to_csv('df5.csv')
        self.df6.to_csv('df6.csv')
        self.df7.to_csv('df7.csv')
        self.df8.to_csv('df8.csv')
        self.df9.to_csv('df9.csv')
    
    def __del__():
        print('удаление')
        
def main():
    poker = poker_t('pok.tr.csv')
    poker.sravn()
    
if __name__ == '__main__':
    main()
    #te:
    #0- 
    #1- пара(две карты одинакового анга)
    #2
    #3- тройка(три карты одного ранга)
    #4
    #5
    #6
    #7