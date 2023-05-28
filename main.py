from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from colorama import Fore
import os, json

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

with open("config.json")as jsonfile:
    conf = json.load(jsonfile)
title = conf["title"]

for file in os.listdir('routes'):
    if file.endswith('.py') and file != '__init__.py':
        module_name = file[:-3]
        module = __import__(f'routes.{module_name}', fromlist=[module_name])
        router = getattr(module, 'router')
        app.include_router(router)

templates = Jinja2Templates(directory="templates")

if __name__ == '__main__':
    print(Fore.GREEN + """
===========================================
================PTEROCLIENT================
===========================================""")
    print(Fore.BLUE + "\n\nGitHub : https://github.com/BreadCatto/PteroClient")
    print(Fore.BLUE + "Copyright (c) 2023 Jay Kumar \nLicensed Under a MIT License.")
    import uvicorn
    uvicorn.run("main:app", host=conf["host"], port=conf["port"], reload=True)