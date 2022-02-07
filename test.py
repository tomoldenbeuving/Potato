#%%
from maps import map
from GPS import locatie
import pandas as pd
import folium
import time
import serial
import io



#%%


i=0
while i<10:
    df1 = pd.DataFrame(locatie()).T
    df2 = pd.DataFrame(locatie()).T
    df1 = pd.concat([df1,df2])
    i+=1

print(df1)
