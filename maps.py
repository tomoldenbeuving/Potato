#%%
import pandas as pd
from datamangement import merge_data
import folium
#functie om de verschillende datasets samen te voegen en te sorteren op een specifieke kolom


df = merge_data('data.csv', 'data2.csv', "time")
m = folium.Map(location=[52.166665, 5.398278], zoom_start=13)
for i in range(0,len(df)):
   folium.Marker(
      location=[df.iloc[i]['lat'], df.iloc[i]['lon']],
      popup=df.iloc[i]['name']
   ).add_to(m)
m
# %%
