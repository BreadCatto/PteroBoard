import pymongo
import bcrypt
import json

with open("config.json") as jsonfile:
    conf = json.load(jsonfile)

client = pymongo.MongoClient(conf["app"]["mongodb_url"])
db = client.get_database('pteroclient')
records = db.users
resources = db.resources

default_pkg = conf["packages"]["default_pkg"]

async def create(email, password, username, pteroid):
    records_json = {
        "username": username,
        "email": email,
        "password": password,
        "pterodactyl_id": pteroid,
        "package": default_pkg,
        "verified": False
    }
    resources_json = {
        "username": username,
        "coins": 0,
        "cpu": 0,
        "ram": 0,
        "disk": 0,
        "servers": 0,
        "backups": 0,
        "databases": 0,
        "ports": 0
    }

    user_inserted = await records.insert_one(records_json)
    resources_inserted = await resources.insert_one(resources_json)
