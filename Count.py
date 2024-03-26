from helper import *

# open file
with open("eventstext.txt", "r") as file:

    read = file.read()

    read = read.replace('â', '').replace('€', '').replace('™','')

    for abv in ABV :
        read = read.replace(abv, ABV[abv])

    for street in AS :
        print(street, read.count(street))