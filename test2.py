from maps import map
from GPS import locatie
import pandas as pd
import folium
import time

df = pd.read_csv('data.csv')

df2 = pd.DataFrame(locatie())

df2 = df2[' '].str.split(',')

df = pd.concat([df,df2])

print(df)