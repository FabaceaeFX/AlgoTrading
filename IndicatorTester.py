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
    
      #  self.WinsAndLossesCounter = _WinsAndLossesCounter
        self.MoneyManager         = _MoneyManager
        self.CSV_Reader           = _CSV_Reader
        self.TradeOrderManager    = _TradeOrderManager
        self.WinOrLossArbiter     = _WinOrLossArbiter
        self.DataVisualizer       = _Data_Visualizer
        
        self.Data                 = None
        
        self.StartingDay          = par.StartingDay
        self.LastDay              = par.LastDay
        
        self.TradeOrder           = None
        self.CurrentTrade         = None
        
        self.StopLoss             = None
        self.TakeProfit           = None
        
        self.Wins                 = 0
        self.Losses               = 0
        
     
        
    def LoopOverTradingDays(self):
    
        
        Datas = self.CSV_Reader.ReadCSVFile('tsla.csv')
        self.Data = Datas.to_numpy()
        

       
    
        for day in range (self.StartingDay, self.LastDay):
        

            
            self.TradeOrder = self.TradeOrderManager.getTradeOrder(self.Data[day,:],
                             self.CurrentTrade)
                             
            
            
            if self.TradeOrder == 'buy':
            
                self.putStopLossAndTakeProfit(self.Data[day,6],
                                              self.TradeOrder, 
                                              self.Data[day,8])
            
                self.CurrentTrade = 'bought'
                
            if self.TradeOrder == 'sell':
            
                self.putStopLossAndTakeProfit(self.Data[day,6],
                                              self.TradeOrder, 
                                              self.Data[day,8])
                self.CurrentTrade = 'sold'
            
            else:
                pass
                
            Win,Loss=self.WinOrLossArbiter.ArbitIfWinOrLoss(self.Data[day,6],self.CurrentTrade,self.StopLoss,self.TakeProfit)
            self.Wins += Win
            self.Losses += Loss
            
            print('Day:', self.Data[day,0], self.TradeOrder,'Adj Close',self.Data[day, 6], 'StopLoss', self.StopLoss, 'TakeProfit', 
                       self.TakeProfit, 'ATRValue', self.Data[day,8])
            
        print('TOTAL WINS:', self.Wins, 'TOTAL LOSSES', self.Losses, 'WIN TO LOSS RATIO:', self.Wins/self.Losses)
        
       # self.DataVisualizer.PlotData(self.Data)
                
           #print(Data)
            #print('Day:', self.Data[day,0], TradeOrder,'Adj Close',self.Data[day, 4], 'StopLoss', self.StopLoss, 'TakeProfit', 
                       # self.TakeProfit, 'ATRValue', self.Data[day,6])
                
        #print(self.Wins, self.Losses)
                
                
                
    def putStopLossAndTakeProfit(self, _closingPrice, _TradeOrder, _ATRValue ):
      
        self.StopLoss, self.TakeProfit = self.MoneyManager.PutStopLossAndTakeProfit(_closingPrice, _TradeOrder, _ATRValue)
               

        
        
if __name__ == '__main__':

    myMoneyManager          = mm.MoneyManager()
    myParameters            = par
    
    mySMA_Calculator = sma.SMA_Calculator()
    myEMA_Calculator = ema.EMA_Calculator()
    myATR_Calculator = atr.ATR_Calculator(myEMA_Calculator)
    myData_Visualizer = dv.Data_Visualizer()
    myCSV_Reader = cr.CSV_Reader(mySMA_Calculator, myATR_Calculator)
    myTradeOrderManager = tom.TradeOrderManager()
    myWinOrLossArbiter  = wla.WinOrLossArbiter()
    
    
    myIndicatorTester       = IndicatorTester(myMoneyManager,
                                myCSV_Reader, myParameters, myTradeOrderManager,
                                myWinOrLossArbiter, myData_Visualizer)
    myIndicatorTester.LoopOverTradingDays()

