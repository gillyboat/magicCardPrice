import os
import numpy as np
from numpy import loadtxt
from numpy import savetxt
import json

f = os.path.join("cardList")
print(f)

cardList = []

with open(f, 'r') as file:
    print("FILE", file)
    json_data = file.read()
    cardList = json_data

print(cardList)