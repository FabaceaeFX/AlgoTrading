'''

Title: Indicator Seeker 
Autor: Philippe Lehmann
Date:  23/02/2021

'''

import MoneyManager         as mm

import CSV_Reader           as cr
import Parameters           as par

import SMA_Calculator  as sma
import ATR_Calculator  as atr
import EMA_Calculator  as ema
import TradeOrderManager as tom
import WinOrLossArbiter  as wla
import Data_Visualizer as dv

class IndicatorTester:

    def __init__(self, _MoneyManager, _CSV_Reader, _Parameters, _TradeOrderManager,
                        _WinOrLossArbiter, _Data_Visualizer):
    
    
        self.MoneyManager         = _MoneyManager
        self.CSV_Reader           = _CSV_Reader
        self.TradeOrderManager    = _TradeOrderManager
        self.WinOrLossArbiter     = _WinOrLossArbiter
        self.DataVisualizer       = _Data_Visualizer
       
        self.tradeOrder           = None
    
        self.stopLoss             = None
        self.takeProfit           = None
        
        self.totalWins            = 0
        self.totalLosses          = 0
        
     
        
    def LoopOverTradingDays(self):
    
        
        PandaData = self.CSV_Reader.ReadCSVFile('tsla.csv')
        Data = PandaData.to_numpy()
       
    
        for day in range (par.startingDay, par.lastDay):
            self.tradeOrder = self.TradeOrderManager.getTradeOrder(Data[day-1,:], Data[day,:])  
            self.checkForStopLossAndTakeProfit(day, Data)
            win,loss =  self.WinOrLossArbiter.checkIfWinOrLoss(Data[day-1,5], Data[day,5], self.stopLoss, self.takeProfit)
            self.updateTotalWinsAndLosses(win, loss)
            
            print(self.totalWins, self.totalLosses)

                
            
        print('TOTAL WINS:', self.totalWins, 'TOTAL LOSSES', self.totalLosses, 'WIN TO LOSS RATIO:')
        
        self.DataVisualizer.visualizeData(PandaData)
            
            
            
            
   
    def checkForStopLossAndTakeProfit(self, _day, _data):
            
        if self.tradeOrder != None:                   
            self.stopLoss, self.takeProfit = self.MoneyManager.getStopLossAndTakeProfit(_data[_day,5],
                                                                self.tradeOrder, _data[_day,7])            
        else:
            pass
            
            
   
    def updateTotalWinsAndLosses(self, _win, _loss):
                
        if _win or _loss:
        
            self.takeProfit = None
            self.stopLoss   = None
            
            self.totalWins += _win
            self.totalLosses += _loss
            
            

                
    
               

        
        
if __name__ == '__main__':

    myMoneyManager          = mm.MoneyManager()
    myParameters            = par
    
    mySMA_Calculator = sma.SMA_Calculator()
    myEMA_Calculator = ema.EMA_Calculator()
    myATR_Calculator = atr.ATR_Calculator()
    myData_Visualizer = dv.Data_Visualizer()
    myCSV_Reader = cr.CSV_Reader()
    myTradeOrderManager = tom.TradeOrderManager()
    myWinOrLossArbiter  = wla.WinOrLossArbiter()
    
    
    myIndicatorTester       = IndicatorTester(myMoneyManager,
                                myCSV_Reader, myParameters, myTradeOrderManager,
                                myWinOrLossArbiter, myData_Visualizer)
    myIndicatorTester.LoopOverTradingDays()

