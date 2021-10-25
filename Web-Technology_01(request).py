import requests

url = "https://stepik.org/favicon.ico"
res = requests.get(url)
print(res.headers['Server'])
