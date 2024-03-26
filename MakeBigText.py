import pandas as pd

from helper import *

events = pd.read_csv('events.csv')

# open file
with open("eventstext.txt", "a") as file:
    for index, row in events.iterrows():
        file.write( str(row['event']).replace('\n', '').lower() )