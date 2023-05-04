#GeeksForGeeks
# import required module
import os
import numpy as np
from numpy import loadtxt
from numpy import savetxt
import json
  
nameMap = []
nameMap.append(["name","ID"])

# assign directory
directory = 'data/Price History/'
 
# iterate over files in
# that directory
for folder in os.listdir(directory):
    # checking if it is a file
    print(folder)
    newDir = directory + folder
    print(newDir)
    for filename in os.listdir(newDir):
        f = os.path.join(newDir, filename)
        print(filename)
        file = open(f)
        data = json.load(file)
        try:
            nameMap.append([data[1]["title"],filename])
        except Exception as err:
            print(f"No Data? {err=}, {type(err)=}")
            

    
savetxt('nameMap.csv', nameMap, delimiter=',', fmt="%s")



        
