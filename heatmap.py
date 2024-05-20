import geopandas as gpd
import geodatasets
import folium
import matplotlib.pyplot as plt

m = folium.Map(location=[40.70, -73.94], zoom_start=10, tiles="CartoDB positron")
m.save("show.html")