import os
import numpy as np
from numpy import loadtxt
from numpy import savetxt
import json
import csv

f = os.path.join("cardList")
print(f)

cardList = []

with open(f, 'r') as file:
    print("FILE", file)
    json_data = file.read()
    cardList = json_data
    cardList = cardList[2:-3].split("','")

data = {}
jsons = []

import pandas as pd

# Parse the CSV

df = pd.read_csv("nameMap.csv")
checkedNames = []
for index, row in df.iterrows():
    if(row['name'] in cardList and not(row['name'] in checkedNames)):
        #print(row['name'])
        data[row["ID"]] = row['name']
        jsons.append(row["ID"])
        checkedNames.append(row['name'])
        
#Check for errors (non-overlap)
checkedNames.sort()
cardList.sort()

for i in range(len(cardList)):
    if cardList[i] != checkedNames[i]:
        print("LIST:", cardList[i] + ".", "CHECKED:", checkedNames[i] + ".")

# Cardlist stores list of cards we care about
# Data JSON stores json:cardname pairs for cards we care about
# Jsons stores a list of all the json files we care about

print("JSONS:", len(jsons))
print("CARDLIST:", len(cardList))

#print(checkedNames)
#print(cardList)
print(jsons)