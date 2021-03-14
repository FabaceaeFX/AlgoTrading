'''
Description:    Runs trades over a period of time
Author:         Riven Hexagon
Creation Date:  14.03.2021
'''

import pandas as pd

import PriceActionCalculator  as pac

class Broker:

    def __init__(self):
        self.dataFrame  = None
        self.praCalc    = pac.PriceActionCalculator()


    def printData(self, _startDate, _endDate):
        print( self.dataFrame.loc[_startDate : _endDate] )


    def loadDataFrame(self, _source):
        self.dataFrame = pd.read_csv(_source, parse_dates=True, index_col=0)


    def addATR(self):
        pass


    def addPriceAction(self):

        self.dataFrame['Action']= self.dataFrame.apply( 
            lambda row: self.praCalc.calcPriceAction( row['High'],
                                                      row['Low']),
                                                      axis=1)
'''
        priceAction1 = [ self.calcPriceAction(hi, lo)  for hi, lo in
                        zip( self.dataFrame['High'],
                             self.dataFrame['Low'] )]
'''

''' END '''

