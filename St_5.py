from collections import Counter as c
import csv

with open('Crimes.csv') as f:
    data = csv.reader(f)
    print(c(row[5] for row in data if '2015' in row[2]).most_common(1)[0][0])