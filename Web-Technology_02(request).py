import requests, re

url = "https://stepik.org/explore"
res = requests.get(url)

# print(res.text)
print(re.findall(r'"(.*css.*)"',res.text)[0])
