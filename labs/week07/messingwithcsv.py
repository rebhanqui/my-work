import csv

FILENAME = "data.csv"
with open(FILENAME, 'rt') as file:
    csvReader = csv.reader(file, delimiter = ',') #delimiter can be anything
    #for line in csvReader: