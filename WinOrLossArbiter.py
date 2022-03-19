'''

Title: Indicator Seeker 
Autor: Philippe Lehmann
Date:  23/02/2021

'''

class WinOrLossArbiter:
    
    def __init__(self):

        pass


    def checkIfWinOrLoss(self, _previousClosingPrice, _currentClosingPrice, _StopLoss, _TakeProfit):
                                   
        Win  = 0
        Loss = 0
        
        
        if _StopLoss == None:
            if _TakeProfit == None:
                pass
                
        else:

    
            if _previousClosingPrice < _TakeProfit:
                
                if _currentClosingPrice > _TakeProfit:
                
                    Win = 1

            if _previousClosingPrice > _TakeProfit:
            
                if _currentClosingPrice < _TakeProfit:
               
                    Win = 1


           
            if _previousClosingPrice < _StopLoss:
                
                if _currentClosingPrice > _StopLoss:
                
                    Loss = 1

            if _previousClosingPrice > _StopLoss:
            
                if _currentClosingPrice < _StopLoss:
               
                    Loss = 1
                
       
        return(Win, Loss)

       




      
