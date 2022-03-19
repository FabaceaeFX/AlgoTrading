'''

Training on Algorithmic Trading

'''

import numpy          as np

import Parameters     as par
import TXT_Reader     as tr
import EMA_Calculator as ema


class ATR_Calculator:


    def __init__(self):


        pass
        
        
        
    def CalculateATR(self, _dates, _highestPrices, _lowestPrices, _closingPrices,
                            _window):
    
        self.highestPrices    = _highestPrices
        self.lowestPrices     = _lowestPrices
        self.closingPrices    = _closingPrices
        
        
        trueRanges            = self.createDateAndTrueRangeArrays(_dates)
        ATRValues             = self.applyEMAOnTrueRanges(trueRanges, _window)
        
        return(ATRValues)
        
        
        
    def createDateAndTrueRangeArrays(self, _dates):
        
         index                = 1
         trueRanges           = np.zeros(len(_dates))
         
         while index < len(_dates):
            
            trueRange         = self.calculateTrueRange(index)
            trueRanges[index] = trueRange
            
            index += 1
         
         return trueRanges
         
          
    def calculateTrueRange(self, _index):
    
        Range1 = self.highestPrices[_index] - self.lowestPrices[_index]
        Range2 = abs(self.highestPrices[_index] - self.closingPrices[_index-1])
        Range3 = abs(self.lowestPrices[_index] - self.closingPrices[_index-1])

        if Range2 <= Range1 >= Range3:

            trueRange = Range1

        elif Range1 <= Range2 >= Range3:

            trueRange = Range2

        elif Range1 <= Range3 >= Range2:

            trueRange = Range3
            
        return trueRange   
            
            
            
    def applyEMAOnTrueRanges(self, _trueRanges, _window):
        
        ATRValues = ema.EMA_Calculator().CalculateEMA(_trueRanges, 
                                         _window, -1)
                                         
        return ATRValues
        
        
        
        
 
            
