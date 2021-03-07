'''

Training on Algorithmic Trading

'''

import numpy as np

class TXT_Reader():

    def __init__(self):
        
        self.TXT_Data  = None
        self.SplitData = None
        
        self.Dates           = []                    
        self.HighestPrices   = [] 
        self.LowestPrices    = []
        self.OpeningPrices   = []
        self.ClosingPrices   = []
        self.Volumes         = []
        self.AdjustedPrices  = []
        
    def ReadTXTFile(self, _FileName):

        self.OpenTXTFile(_FileName)
        self.SplitTheData()
        self.GetDataValues()
        
        print(self.Dates,
        self.HighestPrices,
        self.LowestPrices,
        self.OpeningPrices,
        self.ClosingPrices,
        self.Volumes,
        self.AdjustedPrices)
        
        return(self.Dates,
        self.HighestPrices,
        self.LowestPrices,
        self.OpeningPrices,
        self.ClosingPrices,
        self.Volumes,
        self.AdjustedPrices)


    def OpenTXTFile(self, _FileName):

        self.TXT_Data = open(_FileName, 'r').read()
   
        
    def SplitTheData(self):

        self.SplitData = self.TXT_Data.split('\n')
    

    def GetDataValues(self):
     
        FullText = np.loadtxt(self.SplitData, delimiter=',', unpack=True)
        self.Dates          = FullText[0]
        self.HighestPrices  = FullText[1]
        self.LowestPrices   = FullText[2]
        self.OpeningPrices  = FullText[3]
        self.ClosingPrices  = FullText[4]
        self.Volumes        = FullText[5]
        self.AdjustedPrices = FullText[6]
        
        
if __name__ == '__main__':

    myTXT_Reader = TXT_Reader()
    myTXT_Reader.ReadTXTFile('tsla.txt')
        
     
        
        
        
