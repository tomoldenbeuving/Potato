# %%
import folium
import pandas as pd
# Build the default map for a specific location
m = folium.Map(location=[52.166665, 5.398278], zoom_start=23)
# Make a data frame with dots to show on the map
df1 = pd.read_csv("data.csv")
df2 = pd.read_csv("data2.csv")
df1
# add marker one by one on the map
for i in range(0,len(df1)):
   folium.Marker(
      location=[df1.iloc[i]['lat'], df1.iloc[i]['lon']],
      popup=df1.iloc[i]['name'],
   ).add_to(m)
# Show the map again
m
#%%