import requests
import json

with open("config.json") as jsonfile:
    data = json.load(jsonfile)

domain = "https://panel.duckhost.pro"
api = ""
url = f'{domain}/api/application/users/2?include=servers'
headers = {
        "Authorization": f"Bearer {api}",
        "Accept": "application/json",
        "Content-Type": "application/json",
        }


response = requests.get(url, headers=headers).json()
das = response["attributes"]["relationships"]["servers"]["data"]

for das in das:
    print(das["attributes"]["name"])