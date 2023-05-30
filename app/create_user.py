import requests
import json

with open("config.json") as jsonfile:
    data = json.load(jsonfile)

domain = data['pterodactyl']['domain']
api = data['pterodactyl']['api_key']
url = f'{domain}/api/application/users'
headers = {
        "Authorization": f"Bearer {api}",
        "Accept": "application/json",
        "Content-Type": "application/json",
        }

async def email_check(email):
    params = {
        "filter[email]": email
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        users = response.json()["data"]
        if len(users) > 0:
            return "exist"

    return "noexist"

async def username_check(username):
    params = {
        "filter[username]": username
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        users = response.json()["data"]
        if len(users) > 0:
            return "exist"

    return "noexist"


async def create(email, username, password):
    payload = '''{
        "email": "%s",
        "username": "%s",
        "first_name": "%s",
        "last_name": "User",
        "password": "%s"
    }''' % (email, username, username, password)
    response = requests.request('POST', url, data=payload, headers=headers)

    if response.status_code == 201:
        res = response.json()
        ptero_id = res["attributes"]["id"]
        return ptero_id
    else:
        print(response.text) 
        return "error"

