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

data = {}
jsons = []

import pandas as pd

# Parse the CSV

df = pd.read_csv("nameMap.csv")
print(df.head())

for index, row in df.iterrows():
    if(row['name'] in cardList):
        data[row["ID"]] = row['name']
        jsons.append(row["ID"])

# Cardlist stores list of cards we care about
# Data JSON stores json:cardname pairs for cards we care about
# Jsons stores a list of all the json files we care about