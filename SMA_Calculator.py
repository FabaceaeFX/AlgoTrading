'''

Training on Algorithmic Trading

'''

import numpy as np

import Parameters as par

class SMA_Calculator():

    def __init__(self):
        self.window = par.SMA_Window

            
    def CalculateSMA(self, _closingPriceValues):
    
        Weights = self.CalculateWeights()
        SMAValues = self.CalculateSMAValues(Weights, _closingPriceValues)
        
        return(SMAValues)
        
        
    def CalculateWeights(self):
    
        Weights = np.repeat(1, self.window)/self.window
        
        return(Weights)
        
    def CalculateSMAValues(self, _weights, _closingPriceValues):
     
        SMAValues = np.convolve(_closingPriceValues, _weights, 'same')
        return(SMAValues)
        
        
if __name__ == '__main__':

    ClosingPriceValues = [1,2,3,4,5,6,7,8,9,10]
    mySMA_Calculator = SMA_Calculator()
    mySMA_Calculator.CalculateSMA(ClosingPriceValues, 3)
        
            
