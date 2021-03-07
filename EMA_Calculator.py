'''

Training on Algorithmic Trading

'''

import numpy as np


class EMA_Calculator():

    def __init__(self):
        
            pass
            
    def CalculateEMA(self, _closingPriceValues, _window, _weightFactor):
    
        Weights = self.CalculateWeights(_window, _weightFactor)
        EMAValues = self.CalculateEMAValues(Weights, _closingPriceValues)
        
     
        return(EMAValues)
        
        
    def CalculateWeights(self, _window, _weightFactor):
    
        Weights  = np.exp(np.linspace(_weightFactor, 0, _window))
        Weights = Weights[::-1]
        Weights /= Weights.sum()
        
        
        return(Weights)
        
    def CalculateEMAValues(self, _weights, _closingPriceValues):
     
         EMAValues = np.convolve(_weights, _closingPriceValues, 'same')
         return(EMAValues)
        
        
if __name__ == '__main__':

    ClosingPriceValues = [1,2,3,4,5,6,7,8,9,10]
    myEMA_Calculator = EMA_Calculator()
    myEMA_Calculator.CalculateEMA(ClosingPriceValues, 3, -1)
