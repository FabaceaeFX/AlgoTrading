'''

Training on Algorithmic Trading

'''

import datetime as dt
import pandas as pd

import CSV_Reader      as cr

import SMA_Calculator  as sma
import ATR_Calculator  as atr
import EMA_Calculator  as ema


class IndicatorHandler:

    def __init__(self, _CSV_Reader, _ATR_Calculator, _SMA_Calculator, _EMA_Calculator):
    
        self.CSVReader     = _CSV_Reader
        
        self.CSV_Data      = None
    
        self.ATRCalculator = _ATR_Calculator
        self.SMACalculator = _SMA_Calculator
        self.EMACalculator = _EMA_Calculator
        
        
    def addIndicatorValuesToData(self)
    
        self.CSV_Data = self.CSVReader.ReadCSVFile()
        self.CSV_Data['ATR'] = self.ATRCalculator.CalculateATR(self.CSV_Data)
        self.CSV_Data['SMA'] = self.SMACalculator.CalculateSMA(self.CSV_Data)
        self.CSV_Data['EMA'] = self.EMACalculator.CalculateEMA(self.CSV_Data)
       
        s
