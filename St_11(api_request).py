import requests
import json

client_id = 'a852b6d647199299ec81'
client_secret = '889f62bdf9cc5c3e9c2780ead45aeef3'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}

ans = {}
with open(r"C:\Users\YaYuBeletskiy\Downloads\dataset_24476_4.txt") as file:
    for line in file.readlines():
        # инициируем запрос с заголовком
        r = requests.get(f"https://api.artsy.net/api/artists/{line.strip()}", headers=headers)

        # разбираем ответ сервера
        j = json.loads(r.text)
        ans[j['sortable_name']] = j['birthday']

for i in sorted(ans.items(), key= lambda it: (it[1], it[0])):
    print(i[0])
