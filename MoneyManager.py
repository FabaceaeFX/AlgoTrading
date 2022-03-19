'''

Title: Indicator Seeker 
Autor: Philippe Lehmann
Date:  23/02/2021

'''

class MoneyManager:

    def __init__(self):

        pass


    def getStopLossAndTakeProfit(self, _CurrentClosingPrice, _TradeOrder, _ATRValue):

        if _TradeOrder == 'buy':
            
            StopLoss   = _CurrentClosingPrice - 1.5*_ATRValue
            TakeProfit = _CurrentClosingPrice + _ATRValue

        if _TradeOrder == 'sell':
        
            StopLoss = _CurrentClosingPrice + 1.5*_ATRValue
            TakeProfit = _CurrentClosingPrice - _ATRValue
         
        if _TradeOrder == None:
        
            pass
            


        return StopLoss,TakeProfit


    

        

    
