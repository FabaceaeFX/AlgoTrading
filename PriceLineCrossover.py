'''

Training on Algorithmic Trading

'''


class PriceLineCrossover:

    def __init__(self):
    
        pass
        
    
    def getTradeOrder(self, _closingPriceValue, _IndicatorValue, _CurrentTrade):
    
        #print('Current Trade:', _CurrentTrade)
    
        if _CurrentTrade == 'sold':
        
            if _closingPriceValue > _IndicatorValue:
                TradeOrder = 'buy'
                
            else:
                TradeOrder = None
                
                
        if _CurrentTrade == 'bought':
            
            if _closingPriceValue < _IndicatorValue:
                 TradeOrder = 'sell'
                 
            else:
                TradeOrder = None
                
        if _CurrentTrade == None:
        
            if _closingPriceValue > _IndicatorValue:
                TradeOrder = 'buy'
              
            if _closingPriceValue < _IndicatorValue:
                TradeOrder = 'sell'
              
             
                      
        return (TradeOrder)
         
if __name__ == '__main__':

    myPriceLineCrossover = PriceLineCrossover()
    myPriceLineCrossover.getTradeOrder(14, 15, 'sold')
