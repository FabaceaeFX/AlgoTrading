'''

Training on Algorithmic Trading

'''

import datetime as dt
import pandas as pd

import Parameters as par

import SMA_Calculator  as sma
import ATR_Calculator  as atr
import EMA_Calculator  as ema


class CSV_Reader:

    def __init__(self, _SMA_Calculator, _ATR_Calculator):
        
        self.SMA_Calculator = _SMA_Calculator
        self.ATR_Calculator = _ATR_Calculator
        
        self.Data           = None
        

        
    def ReadCSVFile(self, _FileName):
    
        self.getCSV_File(_FileName)
        self.AddIndicatorValuesToCSV()
     
        return(self.Data)
    
    def getCSV_File(self, _FileName):
    
        self.Data = pd.read_csv(_FileName, parse_dates=True,  index_col=0)
        
    def AddIndicatorValuesToCSV(self):

        self.Data['SMA20'] = self.SMA_Calculator.CalculateSMA(self.Data['Close']) #window mittelwert über n=5 tage
        self.Data['ATR'] = self.ATR_Calculator.CalculateATR(self.Data.index, self.Data['High'],
                        self.Data['Low'], self.Data['Close'])
        

        
        
if __name__ == '__main__':

    mySMA_Calculator = sma.SMA_Calculator()
    myEMA_Calculator = ema.EMA_Calculator()
    myATR_Calculator = atr.ATR_Calculator(myEMA_Calculator)
    myCSV_Reader = CSV_Reader(mySMA_Calculator, myATR_Calculator)
    myCSV_Reader.ReadCSVFile('tsla.csv')
        
     
        
        
        
