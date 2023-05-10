import csv
import json
import os
import pandas as pd
from datetime import datetime

csv_file = os.path.join('data/data FINALS BEIJING.csv')

sets = ['BRO', 'DMU', 'MID', 'NEO', 'ONE', 'SNC', 'VOW']

card_json_map = {}
jsons = []

with open(csv_file, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row.pop('name')
        card_json_map[name] = row

json_cardList = card_json_map

f = os.path.join("cardList")

cardList = []

with open(f, 'r') as file:
    json_data = file.read()
    cardList = json_data
    cardList = cardList[2:-3].split("','")

df = pd.read_csv("nameMap.csv")
checkedNames = []
for index, row in df.iterrows():
    if(row['name'] in cardList and not(row['name'] in checkedNames)):
        #print(row['name'])
        card_json_map[row["name"]] = row['ID']
        jsons.append(row["ID"])
        checkedNames.append(row['name'])

#print(json_cardList)
#print(card_json_map)

dailyCardPriceData = {}

for card in json_cardList:
    for set in sets:
        if card_json_map[card] in os.listdir('data/Price History/' + set + '/'):
            with open(os.path.join('data/Price History/' + set + '/', card_json_map[card])) as f:
                sales = json.load(f)
                for sale in sales:
                    if(sale["condition"] == "Near Mint" and sale["variant"] == "Foil" and sale['orderDate'][0:4] == '2023'):
                        
                        saleDate = {'month': sale['orderDate'][5:7], 'day': sale['orderDate'][8:10]}
                        
                        if not card in dailyCardPriceData:
                            dailyCardPriceData[card] = {}
                            
                        if not '2023-' + saleDate['month'] + '-' + saleDate['day'] in dailyCardPriceData[card]:
                            dailyCardPriceData[card]['2023-' + saleDate['month'] + '-' + saleDate['day']] = {'totalPrice':0, 'totalShipping':0, 'totalQuantity':0}
                        
                        dailyCardPriceData[card]['2023-' + saleDate['month'] + '-' + saleDate['day']]['totalPrice'] += sale['purchasePrice'] * sale['quantity']
                        dailyCardPriceData[card]['2023-' + saleDate['month'] + '-' + saleDate['day']]['totalShipping'] += sale['shippingPrice']
                        dailyCardPriceData[card]['2023-' + saleDate['month'] + '-' + saleDate['day']]['totalQuantity'] += sale['quantity']
                        

priceChanges = {}

for card in dailyCardPriceData:
    dates = []
    for date in dailyCardPriceData[card]:
        dates.append(date)
        dailyCardPriceData[card][date]['averagePrice'] = round((dailyCardPriceData[card][date]['totalPrice'] + dailyCardPriceData[card][date]['totalShipping']) / dailyCardPriceData[card][date]['totalQuantity'], 2)
    for i in range(1, len(dates)):
        q = 0
    print(card, json_cardList[card], dailyCardPriceData[card][date]['averagePrice'])