'''

Training on Algorithmic Trading

'''

import datetime as dt
import pandas as pd
import pandas_datareader.data as web

class DataWebReader():
  
    def __init__(self):
        
           pass
           
    def readData(self):
    
        DataAsCSV = self.getDataOutOfWeb()
        print(DataAsCSV, DataAsCSV.head())
        #self.convertDataToCSV(Data)
       


    def getDataOutOfWeb(self):
    
        startDay = dt.datetime(2000,1,1)
        endDay   = dt.datetime(2016, 1, 1)
       

        Data = web.DataReader('TSLA', 'yahoo', startDay, endDay)
        DataAsCSV = Data.to_csv('tsla.csv')
     
        
        

    def convertDataToCSV(self, _Data):
    
        DataAsCSV = _Data.to_csv('tsla.csv')
        
        
if __name__ == '__main__':

    myDataWebReader = DataWebReader()
    myDataWebReader.readData()
    
        
