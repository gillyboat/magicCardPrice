import json
import os
from datetime import datetime

sets = ['BRO', 'DMU', 'MID', 'NEO', 'ONE', 'SNC', 'VOW']

n_check = 0

jsons_to_check = []

dates_cards = {}

with open('jsonArray') as f:
    json_data = f.read()
    jsons_to_check = json_data
    jsons_to_check = jsons_to_check[2:-2].split("', '")
    print(jsons_to_check)

for set in sets:
    # Set the path to the directory containing the JSON files
    json_dir = 'data/Price History/' + set + '/'

    # Create variables to store the total purchase price, total shipping price, and total quantity
    total_purchase_price = 0
    total_shipping_price = 0
    total_quantity = 0

    # Get a list of all the JSON files in the directory

    # Loop over each file and extract the purchase price, shipping price, and quantity from each sale
    q = 0
    for file_index in range(len(jsons_to_check)):
        file_name = jsons_to_check[file_index]
        if not file_name.endswith('.json'):
            file_name += '.json'  # add .json extension if not present
        try:
            with open(os.path.join(json_dir, file_name)) as f:
                sales = json.load(f)
                for sale in sales:
                    if(sale["condition"] == "Near Mint" and sale["variant"] == "Foil"):
                        purchase_price = sale['purchasePrice']
                        shipping_price = sale['shippingPrice']
                        quantity = sale['quantity']
                        saleDate = datetime.fromisoformat(sale["orderDate"])
                        
                        if not dates_cards['2023-' + saleDate.month + '-' + saleDate.day]:
                            dates_cards['2023-' + saleDate.month + '-' + saleDate.day] = 0
                    
                        # Add the purchase price, shipping price, and quantity to the total
                        dates_cards['2023-' + saleDate.month + '-' + saleDate.day] += purchase_price * quantity
                        total_shipping_price += shipping_price * quantity
                        total_quantity += quantity
        except:
            q += 1
    
    n_check += len(jsons_to_check) - q
    # Calculate the average purchase price and average shipping price per unit sold
    if total_quantity > 0:
        avg_purchase_price_per_unit = total_purchase_price / total_quantity
        avg_shipping_price_per_unit = total_shipping_price / total_quantity
    else:
        avg_purchase_price_per_unit = 0
        avg_shipping_price_per_unit = 0

    #print(jsons_to_check)
    # Print the results
    print(f"Average purchase price per unit sold in " + set + f": ${avg_purchase_price_per_unit:.2f}")
    print(f"Average shipping price per unit sold in " + set + f": ${avg_shipping_price_per_unit:.2f}")