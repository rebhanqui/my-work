import json

electricBill = {
    'name' : 'Andrew',
    'amount' : '99999'
}

with open("storeData.json", 'wt') as f:
    json.dump(electricBill, f) 