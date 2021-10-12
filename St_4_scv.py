import csv
with open("Crimes.csv") as f:
    file = csv.reader(f)
    primary = [row[5] for row in file if "2015" in row[2]]
    p_count = [primary.count(i) for i in primary]
    print(p_count)
    print(primary)
    print(primary[p_count.index(max(p_count))])