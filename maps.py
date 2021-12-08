import pandas as pd
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame

#pandas bestand uitlezen
df = pd.read_csv("data.csv", delimiter=',', skiprows=0)

#gff testen hoe github werkt
#hieronder is alleemaal specifiek voor de kaart module
#geometry = [Point(xy) for xy in zip(df['Longitude'], df['Latitude'])]
#gdf = GeoDataFrame(df, geometry=geometry)   

#this is a simple map that goes with geopandas
#world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
#gdf.plot(ax=world.plot(figsize=(10, 6)), marker='o', color='red', markersize=15);

#df.longitude.min(5.39442), df.longitude.max(5.39892),      
#df.latitude.min(52.16532), df.latitude.max(52.16814)
