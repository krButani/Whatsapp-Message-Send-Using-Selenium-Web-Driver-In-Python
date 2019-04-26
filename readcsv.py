import time
import csv
import os

with open('people.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
       print(row)

csvFile.close()