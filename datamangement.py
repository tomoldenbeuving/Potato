import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import time 


def merge_data(data1, data2, sorteren_op): 
        df1 = pd.read_csv(data1)
        df1 = df1.sort_values(by=sorteren_op)      
        
        df2 = pd.read_csv(data2)
        df2 = df2.sort_values(by=sorteren_op)

        df3 = pd.merge_asof(df1, df2,on="time", direction="nearest")
 #       df3.to_csv(path_or_buf="data_destination.csv", index=False)
        return df3

