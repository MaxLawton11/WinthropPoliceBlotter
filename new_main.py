import osmnx as ox
import matplotlib.pyplot as plt
import itertools

import pandas as pd

# Define the location and the street name you want to highlight
place_name = "Winthrop, Massachusetts"

# Download the street network for the specified area
G = ox.graph_from_place(place_name, network_type='drive')

# Get edges (streets) dataframe
edges = ox.graph_to_gdfs(G, nodes=False)

df = pd.DataFrame(
    {
        'name'   : edges['name'],
        'length' : edges['length']
    }
)

print(df)

# Identify the edges that correspond to the specific street
highlights = []

# Plot the street network
fig, ax = ox.plot_graph(G, show=False, close=False)


def hs(s,c) :
    highlights.append( (edges[edges['name'] == s], c) )

hs('Main Street', 'b')
hs('Bartlett Road', 'r')
hs('Winthrop Street', 'g')

for highlight, color in highlights :
    highlight.plot(ax=ax, linewidth=4, edgecolor=color)

# Show the plot
plt.show()
