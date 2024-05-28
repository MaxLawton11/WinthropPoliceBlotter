import random
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
    color = random.choice(
        [
            "b", "g", "r", "c", "m", "y", "k", "w", "aliceblue", "antiquewhite",
    "aqua", "aquamarine", "azure", "beige", "bisque", "black", "blanchedalmond",
    "blue", "blueviolet", "brown", "burlywood", "cadetblue", "chartreuse",
    "chocolate", "coral", "cornflowerblue", "cornsilk", "crimson", "cyan",
    "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgreen",
    "darkgrey", "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange",
    "darkorchid", "darkred", "darksalmon", "darkseagreen", "darkslateblue",
    "darkslategray", "darkslategrey", "darkturquoise", "darkviolet", "deeppink",
    "deepskyblue", "dimgray", "dimgrey", "dodgerblue", "firebrick", "floralwhite",
    "forestgreen", "fuchsia", "gainsboro", "ghostwhite", "gold", "goldenrod",
    "gray", "green", "greenyellow", "grey", "honeydew", "hotpink", "indianred",
    "indigo", "ivory", "khaki", "lavender", "lavenderblush", "lawngreen",
    "lemonchiffon", "lightblue", "lightcoral", "lightcyan", "lightgoldenrodyellow",
    "lightgray", "lightgreen", "lightgrey", "lightpink", "lightsalmon",
    "lightseagreen", "lightskyblue", "lightslategray", "lightslategrey",
    "lightsteelblue", "lightyellow", "lime", "limegreen", "linen", "magenta",
    "maroon", "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple",
    "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise",
    "mediumvioletred", "midnightblue", "mintcream", "mistyrose", "moccasin",
    "navajowhite", "navy", "oldlace", "olive", "olivedrab", "orange", "orangered",
    "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred",
    "papayawhip", "peachpuff", "peru", "pink", "plum", "powderblue", "purple",
    "rebeccapurple", "red", "rosybrown", "royalblue", "saddlebrown", "salmon",
    "sandybrown", "seagreen", "seashell", "sienna", "silver", "skyblue", "slateblue",
    "slategray", "slategrey", "snow", "springgreen", "steelblue", "tan", "teal",
    "thistle", "tomato", "turquoise", "violet", "wheat", "white", "whitesmoke",
    "yellow", "yellowgreen"
        ]
    )

    hs(f"{s}", color)

hs('Main Street', 'b')
hs('Bartlett Road', 'r')
hs('Winthrop Street', 'g')

for highlight, color in highlights :
    highlight.plot(ax=ax, linewidth=4, edgecolor=color)

# Show the plot
plt.show()
