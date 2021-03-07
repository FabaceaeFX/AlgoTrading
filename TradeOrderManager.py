'''

Training on Algorithmic Trading

'''
import PriceLineCrossover as plc

import Parameters as par

class TradeOrderManager:

    def __init__(self):
        
        self.IndicatorType = par.IndicatorType
        self.CurrentTrade  = None 
        
        self.PriceLineCrossover = plc.PriceLineCrossover()
        
        self.Date            = 0                   
        self.HighestPrice    = 0 
        self.LowestPrice     = 0
        self.OpeningPrice    = 0
        self.ClosingPrice    = 0
        self.Volume          = 0
        self.AdjustedPrice   = 0
        self.ATR             = 0
        self.SMA20           = 0
        
        self.TradeOrder      = None
        
    def getTradeOrder(self, _Data, _CurrentTrade):
    
    
        self.Date            = _Data[0]                  
        self.HighestPrice    = _Data[1]
        self.LowestPrice     = _Data[2]
        self.OpeningPrice    = _Data[3]
        self.ClosingPrice    = _Data[4]
        self.AdjustedPrice   = _Data[5]
        self.ATR             = _Data[6]
        self.SMA20           = _Data[7]
        
        self.CurrentTrade = _CurrentTrade
        
        self.fetchTradeOrder()
        
        return(self.TradeOrder)
        
    def fetchTradeOrder(self):
    
        if self.IndicatorType == 'PriceLineCrossover':
        
            self.TradeOrder = self.PriceLineCrossover.getTradeOrder(self.ClosingPrice, self.SMA20, self.CurrentTrade)

