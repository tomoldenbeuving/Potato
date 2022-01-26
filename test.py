#%%
from maps import map
from GPS import loc
import pandas as pd
import folium
import time

df = pd.DataFrame({
    "time":[loc.time()],
    "lat":[loc.lat()],
    "lon":[loc.lon()]
})
print(df)
time.sleep(10)


df = df.append({
    "time":loc.time(),
    "lat":loc.lat(),
    "lon":loc.lon()
},ignore_index=True)

print(df)

#%%

map("data.csv", "data2.csv")

#%%