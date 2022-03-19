'''
Description:    Program entry point
Author:         Riven Hexagon
Creation Date:  14.03.2021
'''

import pandas as pd

import Broker as bro        # yo bro!


if __name__ == '__main__':

    myBroker    = bro.Broker()

    startDate   = None
    endDate     = "20100715"
    source      = 'tsla50.csv'

    myBroker.loadDataFrame( source )
    myBroker.addPriceAction()
    myBroker.printData( startDate, endDate )

    #myData = pd.read_csv(source, parse_dates=True,  index_col=0)
    #print( myData.loc["20100629":"20100630", ["High","Low"]] )
    #print( myData.loc["20100827":endDate, ["High","Low"]] )
    #myVal = myData.loc["20100827", ["Low"]]
    #print( myVal.values[0] )
    #print(myData.dtypes)

''' END '''
