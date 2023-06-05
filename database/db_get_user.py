import pymongo
import bcrypt
import json

with open("config.json") as jsonfile:
    conf = json.load(jsonfile)

client = pymongo.MongoClient(conf["app"]["mongodb_url"])
db = client.get_database('pteroclient')
records = db.users
resources = db.resources

def find(email):
    get_username = records.find_one({"email": email})
    username = get_username['username']
    info = resources.find_one({"username": username})
    return info

def check_verified(email):
    get_verified = records.find_one({"email": email})
    verified = get_verified["verified"]
    return verified

def get_info(email):
    get = records.find_one({"email": email})
    return get