'''

Training on Algorithmic Trading

'''

import pandas as pd

import Parameters as par

import SMA_Calculator  as sma
import ATR_Calculator  as atr
import EMA_Calculator  as ema


class CSV_Reader:

    def __init__(self):
        pass
        

        
    def ReadCSVFile(self, _FileName):
    
        Data = pd.read_csv(_FileName, parse_dates=True,  index_col=0)
        Data['SMA20'] = sma.SMA_Calculator().CalculateSMA(Data['Close'], par.SMA_Window) #window mittelwert über n=5 tage
        Data['ATR'] = atr.ATR_Calculator().CalculateATR(Data.index, Data['High'], Data['Low'], Data['Close'], 14)
        
     
        return(Data)
    
 
        
     
        
        
        
