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
    
print(cardList)

data = {}
jsons = []

import pandas as pd

df = pd.read_csv("nameMap.csv")
print(df.head())

for index, row in df.iterrows():
    if(row['name'] in cardList):
        data[row["ID"]] = row['name']
        jsons.append(row["ID"])

print(data)
print(jsons)