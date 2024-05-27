import osmnx as ox
import geopandas as gpd

# Specify the location or area of interest
place_name = "Winthrop, Massachusetts, USA"

# Download the street network data
graph = ox.graph_from_place(place_name, network_type='all')

# Convert the graph to a GeoDataFrame
gdf = ox.graph_to_gdfs(graph, nodes=False, edges=True)

# Calculate the length of each street
gdf['length_m'] = gdf['geometry'].length
print(gdf)

# Print the street names and their lengths
for index, row in gdf.iterrows():
    street_name = row['name']
    length = row['length_m']
    if str(street_name) == "nan" :
        continue
    #print(f"Street: {street_name}, Length: {length} meters")
