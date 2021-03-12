'''

Training on Algorithmic Trading

'''


class PriceLineCrossover:

    def __init__(self):
    
        self.TradeOrder = None
        
    
    def getTradeOrder(self, _previousClosingValue, _currentClosingValue, _prevIndicatorValue, _IndicatorValue):
    
        self.TradeOrder = None
    
        if _previousClosingValue > _prevIndicatorValue:
            if _currentClosingValue < _IndicatorValue:
                print('Ich sollte jetzt verkaufen')
                self.TradeOrder = 'sell'
                
      
        
        if _previousClosingValue < _prevIndicatorValue:
            if _currentClosingValue > _IndicatorValue:
                print('Hier sollte ich kaufen')
                self.TradeOrder = 'buy'
        
        return (self.TradeOrder)
         
if __name__ == '__main__':

    myPriceLineCrossover = PriceLineCrossover()
    myPriceLineCrossover.getTradeOrder(14, 15, 'sold')
