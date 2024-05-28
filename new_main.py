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


streets = {}
for name, length in zip(edges['name'], edges['length'])  :

    # remove pesky nan
    if f"{name}" == 'nan' :
        continue
    
    # nested names [Street1, Street2,... ]
    if type(name) == type([]) :
        for sub_name in name :
            if sub_name in streets :
                streets[sub_name] += length
            else :
                # since these streets are part of a double node, if they don't exist on their own somewhere else on the map, \
                # they can not be plotted independently due to not being a real street.
                # we will add the lengths if they are a true, mappable, independent street, otherwise we don't/can't care about them.
                pass
        continue # end, no need to process normally 

    # for normal name in the list of names
    if name in streets : # if they exsit in the dic, add on to the length
        streets[name] += length
    else : # if it does not exist, set the initial length
        streets[name] = length


# Identify the edges that correspond to the specific street
highlights = []

# Plot the street network
fig, ax = ox.plot_graph(G, show=False, close=False)


def hs(s,c) :
    highlights.append( (edges[edges['name'] == s], c) )

for s in streets :
    print(s)
    hs(f"{s}", 'purple')

hs('Main Street', 'b')
hs('Bartlett Road', 'r')
hs('Winthrop Street', 'g')

for highlight, color in highlights :
    highlight.plot(ax=ax, linewidth=4, edgecolor=color)

# Show the plot
plt.show()
