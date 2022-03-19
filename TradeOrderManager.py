'''

Training on Algorithmic Trading

'''
import PriceLineCrossover as plc
import Parameters as par

class TradeOrderManager:

    def __init__(self):
       
        
        self.PriceLineCrossover = plc.PriceLineCrossover()
        
        
    def getTradeOrder(self, _previousDateRow, _currentDateRow):
 
        
        PrevClosingPrice    = _previousDateRow[3]
        ClosingPrice        = _currentDateRow[3]
       
        
        PrevSMA20           = _previousDateRow[6]
        SMA20               = _currentDateRow[6]

        
        if par.indicatorType == 'PriceLineCrossover':
        
            print('PrevClose:', PrevClosingPrice,'CurrClose:', ClosingPrice, 'PrevSMA:', PrevSMA20, 'CurrSMA:', SMA20)
        
            tradeOrder = self.PriceLineCrossover.getTradeOrder(PrevClosingPrice, ClosingPrice, PrevSMA20, SMA20)
                                                                                    
            print(tradeOrder)

        return(tradeOrder)
    
        
