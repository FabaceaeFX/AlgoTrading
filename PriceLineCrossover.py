'''

Training on Algorithmic Trading

'''


class PriceLineCrossover:

    def __init__(self):
    
        TradeOrder = None
        
    
    def getTradeOrder(self, _previousClosingValue, _currentClosingValue, _prevIndicatorValue, _IndicatorValue):
    
        TradeOrder = None
    
        if _previousClosingValue > _prevIndicatorValue:
            if _currentClosingValue < _IndicatorValue:
                TradeOrder = 'sell'
                
      
        
        if _previousClosingValue < _prevIndicatorValue:
            if _currentClosingValue > _IndicatorValue:
                TradeOrder = 'buy'
        
        return (TradeOrder)
         
if __name__ == '__main__':

    myPriceLineCrossover = PriceLineCrossover()
    myPriceLineCrossover.getTradeOrder(14, 15, 'sold')
