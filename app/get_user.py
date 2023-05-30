import requests
import json
import pymongo

with open("config.json") as jsonfile:
    data = json.load(jsonfile)

client = pymongo.MongoClient(data["app"]["mongodb_url"])
db = client.get_database('pteroclient')
records = db.users
resources = db.resources

domain = data['pterodactyl']['domain']
api = data['pterodactyl']['api_key']
url = f'{domain}/api/application/users'
headers = {
        "Authorization": f"Bearer {api}",
        "Accept": "application/json",
        "Content-Type": "application/json",
        }

def find(email):
    get_info = records.find_one({"email": email})
    ptero_id = get_info["pterodactyl_id"]
    get_url = f"{url}/{ptero_id}"
    res = requests.get(get_url, headers=headers).json()
    return res

