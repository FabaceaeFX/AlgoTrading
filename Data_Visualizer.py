import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd

class Data_Visualizer:

    def __init__ (self):
    
        pass

    def visualizeData(self, _Data):
    
        print(_Data)
    
        plt.style.use('ggplot')

        _Data.index.name = 'Date'
      
        IndicatorPlots =  [ mpf.make_addplot(_Data['SMA20']),
                        mpf.make_addplot(_Data['ATR'],panel=1,color='g')]
        
        mpf.plot(_Data,addplot=IndicatorPlots,type='candle')



