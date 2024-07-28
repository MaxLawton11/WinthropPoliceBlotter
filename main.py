import random
import osmnx as ox
import matplotlib.pyplot as plt
import pandas as pd
from bs4 import BeautifulSoup
import requests

# download a map of the town
# get the 'edges' (aka roads)
place_name = "Winthrop, Ma"
G = ox.graph_from_place(place_name, network_type='drive')
edges = ox.graph_to_gdfs(G, nodes=False)


# make list of streets
# we will store a dic of both the name, and the lengt of the street
# the lenght will be to total lentght of all of the nodes
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


# find all of the police blotter urls
# they were put in by hand, so there really isn't a system or pattern
# this means that we basically need to try them all since 2009...
urls_are_preprocessed = True
if not urls_are_preprocessed :
    # add code for finding urls later
    exit("No URLs")


# scrpae all of the events into one big csv file
# go throught all of the found urls, and extract the events
events_are_preprocessed = True
if not events_are_preprocessed :
    # add code for compliting events later
    exit("No events")

# count all of the instances of the street name in the events.csv file
streets_incident_number={} # track amount of incidents per street
with open("events.csv", "r") as file: #open the file
    read = file.read()
    read = read.replace('â', '').replace('€', '').replace('™','')

    for srt in streets :
        count = read.count(srt)
        streets_incident_number[srt] = count


# find the most amount of inceidents on one street
streets_incident_per_length = {}
max_incidents = 0
for srt in streets :
    ipl = streets_incident_number[srt]/streets[srt]
    streets_incident_per_length[srt] = ipl

    if ipl>max_incidents :
        max_incidents = ipl

for s in streets_incident_number :
    print(s, streets_incident_number[s], streets_incident_per_length[s],  streets_incident_per_length[s]/max_incidents)


# Identify the edges that correspond to the specific street
highlights = []

# Plot the street network
fig, ax = ox.plot_graph(G, show=False, close=False)

def hs(s,c) :
    highlights.append( (edges[edges['name'] == s], c) )

def value_to_color(value):
    """Returns an RGB color value transitioning from green (0) to yellow (0.5) to red (1) based on input value (0 to 1)."""
    if not 0 <= value <= 1:
        raise ValueError("Value must be between 0 and 1")
    if value <= 0.5:
        # Transition from green to yellow
        red = 2 * value  # Increase red component more sharply
        green = 1-red
        blue = 0
    else:
        # Transition from yellow to red
        green = 2 * (1 - value)  # Decrease green component more gradually
        red = 1-green
        blue = 0
    return (red, green, blue)

for s in streets :
    c = value_to_color( streets_incident_per_length[s]/max_incidents)
    hs(f"{s}", c)


for highlight, color in highlights :
    highlight.plot(ax=ax, linewidth=4, edgecolor=color)

# Show the plot
plt.show()
