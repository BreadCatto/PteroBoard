import pymongo
import bcrypt
import json

with open("config.json") as jsonfile:
    conf = json.load(jsonfile)

client = pymongo.MongoClient(conf["mongodb_url"])
db = client.get_database('pteroclient')
records = db.users

def create(email, password, username, fname, lname, pteroid):
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    create_json = {
        "first_name": fname,
        "last_name": lname,
        "username": username,
        "email": email,
        "password": hashed,
        "pterodactyl_id": pteroid
    }
    inserted = records.insert_one(create_json)
