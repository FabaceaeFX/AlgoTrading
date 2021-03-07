'''

Training on Algorithmic Trading

'''

import datetime as dt
import pandas as pd
import pandas_datareader.data as web

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as tic

#from matplotlib.finance import candlestick_ohlc




class Data_Visualizer():

    def __init__(self):
    
        pass
        
    def PlotData(self, _Data):
        
        ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
        
        fin.candlestick_ohlc(ax1, _Data)
        
        plt.show()
    

if __name__ == '__main__':

    myData_Visualizer = Data_Visualizer()
    myData_Visualizer.ReadTXTFile()
    
    
'''        ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
        ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
        
        ax1.xaxis_date()
        
        ax1.plot(_Data.index, _Data['Close'])
        ax1.plot(_Data.index, _Data['SMA20'])
        ax2.plot(_Data.index, _Data['ATR'] )
       
    
       
    
        mpf.plot(_Data, type='candle')
        '''
