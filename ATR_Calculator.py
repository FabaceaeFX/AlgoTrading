'''

Training on Algorithmic Trading

'''

import numpy          as np
import TXT_Reader     as tr
import EMA_Calculator as ema
import Parameters     as par

class ATR_Calculator:

    def __init__(self, _EMA_Calculator):
    
      
        self.EMA_Calculator  = _EMA_Calculator
        self.TrueRange       = None
        self.TrueRangeDates  = []
        self.TrueRanges      = []
        self.ATR_Values      = []
        
        self.Dates           = []                    
        self.HighestPrices   = [] 
        self.LowestPrices    = []
        self.ClosingPrices   = []
        self.Window          = 0

        
        
        
    def CalculateATR(self, _Data):
    
        self.Dates           = _Data.index  
        self.HighestPrices   = _Data['High']
        self.LowestPrices    = _Data['Low']
        self.ClosingPrices   = _Data['Close']
        self.Window          = par.ATR_Window
        
        
        self.CreateDateAndTrueRangeArrays()
        self.ApplyEMAOnTrueRanges()
        
        return(self.ATR_Values)
        
        
        
    def CreateDateAndTrueRangeArrays(self):
        
         index = 1
         self.TrueRanges.append(0)
         
         while index < len(self.Dates):
            
            self.CalculateTrueRange(index)
            self.TrueRanges.append(self.TrueRange)
            
            index += 1
         
          
    def CalculateTrueRange(self, _index):
    
        Range1 = self.HighestPrices[_index]-self.LowestPrices[_index]
        Range2 = abs(self.HighestPrices[_index]-self.ClosingPrices[_index-1])
        Range3 = abs(self.LowestPrices[_index]-self.ClosingPrices[_index-1])

        if Range2 <= Range1 >= Range3:

            self.TrueRange = Range1

        elif Range1 <= Range2 >= Range3:

            self.TrueRange = Range2

        elif Range1 <= Range3 >= Range2:

            self.TrueRange = Range3
            
            
            
    def ApplyEMAOnTrueRanges(self):
        
        self.ATR_Values = self.EMA_Calculator.CalculateEMA(self.TrueRanges, 
                                         self.Window, -1)
                                         
                                         

     
if __name__ == '__main__':

    myEMA_Calculator = ema.EMA_Calculator()
    myATR_Calculator = ATR_Calculator(myEMA_Calculator)
    myATR_Calculator.CalculateATR()
            
