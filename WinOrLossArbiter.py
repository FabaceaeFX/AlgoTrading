'''

Title: Indicator Seeker 
Autor: Philippe Lehmann
Date:  23/02/2021

'''

class WinOrLossArbiter:
    
    def __init__(self):

        pass


    def ArbitIfWinOrLoss(self, _CurrentClosingPrice, _CurrentTrade,
                                   _StopLoss, _TakeProfit):
                                   
        Win  = 0
        Loss = 0
    
        if _CurrentTrade == 'bought':
            
            if _CurrentClosingPrice >= _TakeProfit:
            
                Win = 1

            if _CurrentClosingPrice <= _StopLoss:
            
                Loss = 1


        if _CurrentTrade == 'sold':
            
            if _CurrentClosingPrice <= _TakeProfit:
            
                Win = 1

            if _CurrentClosingPrice >= _StopLoss:
            
                Loss = 1
                
        return(Win, Loss)

       




      
