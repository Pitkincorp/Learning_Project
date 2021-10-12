import json
s = []
with open('group_people.json') as fl:
    data = json.load(fl)
for i in data:
    s.append(sum([int(j["year"]) for j in i["people"] if j["gender"]=="Fimale" if int(j["year"])>1977]))
print(s)
# x = s.index(max(s))
# print(f"{data[x]['manager']['first_name']} {data[x]['manager']['last_name']} {s[x]}")
