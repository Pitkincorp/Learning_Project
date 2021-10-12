import requests
with open(r"C:\Users\YaYuBeletskiy\Downloads\dataset_24476_3 (1).txt") as file:
    for line in file.readlines():
        api_url = f"http://numbersapi.com/{line.strip()}/math"
        params = {'json': 'true'}
        res = requests.get(api_url, params=params)

        print("Interesting" if res.json()["found"] else "Boring")
