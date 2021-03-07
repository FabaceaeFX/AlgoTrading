'''

Training on Algorithmic Trading

'''

import numpy as np

import Parameters as par


class SMA_Calculator():

    def __init__(self):
        
            pass
            
    def CalculateSMA(self, _Data):
    
        Weights = self.CalculateWeights(par.SMA_Window)
        SMAValues = self.CalculateSMAValues(Weights, _Data['Close'])
        
        return(SMAValues)
        
        
    def CalculateWeights(self, _window):
    
        Weights = np.repeat(1, _window)/_window
        
        return(Weights)
        
    def CalculateSMAValues(self, _weights, _closingPriceValues):
     
        SMAValues = np.convolve(_closingPriceValues, _weights, 'same')
        return(SMAValues)
        
        
if __name__ == '__main__':

    ClosingPriceValues = [1,2,3,4,5,6,7,8,9,10]
    mySMA_Calculator = SMA_Calculator()
    mySMA_Calculator.CalculateSMA(ClosingPriceValues, 3)
        
            
