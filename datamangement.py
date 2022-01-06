import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import time 


def merge_data(data1, data2, sorteren_op): 
        #opent bestand wat nog gespecificeerd moet worden en sorteert de rijen op de gespecificeerde kolom
        df1 = pd.read_csv(data1)
        df1 = df1.sort_values(by=sorteren_op)      
        
        df2 = pd.read_csv(data2)
        df2 = df2.sort_values(by=sorteren_op)

        #voegd de twee datasets samen op dichtsbijzijnde absolute waarde
        df3 = pd.merge_asof(df1, df2,on="time", direction="nearest")
        #functie geeft de samengevoegde set terug
        return df3

