'''

Training on Algorithmic Trading

'''
import PriceLineCrossover as plc
import numpy as np

import Parameters as par

class TradeOrderManager:

    def __init__(self):
        
        self.IndicatorType = par.IndicatorType
        
        self.PriceLineCrossover = plc.PriceLineCrossover()
        
        
       # self.Date            = 0                   
        self.HighestPrice        = 0
        self.LowestPrice         = 0
        self.OpeningPrice        = 0
        self.ClosingPrice        = 0
        self.Volume              = 0
        self.AdjustedPrice       = 0
        self.SMA20               = 0
        self.ATR                 = 0
        
        self.PrevHighestPrice    = 0
        self.PrevLowestPrice     = 0
        self.PrevOpeningPrice    = 0
        self.PrevClosingPrice    = 0
        self.PrevVolume          = 0
        self.PrevAdjustedPrice   = 0
        self.PrevSMA20           = 0
        self.PrevATR             = 0
        
        self.TradeOrder      = None
        
    def getTradeOrder(self, _previousDateRow, _currentDateRow):
    
        TodaysData      = _currentDateRow
        YesterdaysData  = _previousDateRow    
        
        self.HighestPrice        = TodaysData[0] 
        self.LowestPrice         = TodaysData[1]
        self.OpeningPrice        = TodaysData[2]
        self.ClosingPrice        = TodaysData[3]
        self.Volume              = TodaysData[4]
        self.AdjustedPrice       = TodaysData[5]
        self.SMA20               = TodaysData[6]
        self.ATR                 = TodaysData[7]
        
        self.PrevHighestPrice    = YesterdaysData[0] 
        self.PrevLowestPrice     = YesterdaysData[1]
        self.PrevOpeningPrice    = YesterdaysData[2]
        self.PrevClosingPrice    = YesterdaysData[3]
        self.PrevVolume          = YesterdaysData[4]
        self.PrevAdjustedPrice   = YesterdaysData[5]
        self.PrevSMA20           = YesterdaysData[6]
        self.PrevATR             = YesterdaysData[7] 

        
        self.fetchTradeOrder()
        
        return(self.TradeOrder)
        
    def fetchTradeOrder(self):
    
        if self.IndicatorType == 'PriceLineCrossover':
        
            print('PrevClose:', self.PrevClosingPrice,'CurrClose:', self.ClosingPrice, 'PrevSMA:', self.PrevSMA20, 'CurrSMA:', self.SMA20)
        
            self.TradeOrder = self.PriceLineCrossover.getTradeOrder(self.PrevClosingPrice, self.ClosingPrice, 
                                                                                    self.PrevSMA20, self.SMA20)
                                                                                    
            print(self.TradeOrder)

