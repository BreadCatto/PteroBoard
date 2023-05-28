from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pymongo
import bcrypt
import json
from database import user_make

with open("config.json") as jsonfile:
    conf = json.load(jsonfile)
title = conf["title"]

client = pymongo.MongoClient(conf["mongodb_url"])
db = client.get_database('pteroclient')
records = db.users

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "title": title + " Login"})
