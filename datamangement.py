import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

data = {"employee":"Fred",
        "group":"niksen"}

data2 = {"employee":"Fred",
            "hire_date":""}

df1 = pd.read_csv("data.csv")
df2 = pd.read_csv("data2.csv")

df1 = df1.append(data, ignore_index=True)
df2 = df2.append(data2, ignore_index=True)

df3 = pd.merge_asof(df1, df2)
print(df3)