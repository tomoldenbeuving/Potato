from maps import map
from GPS import loc
import pandas as pd

#%%
map("data.csv", "data2.csv")

#%%


df = pd.DataFrame({
    "time":[loc.time()],
    "lat":[loc.lat()]
})

print(df)