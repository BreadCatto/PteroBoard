from flask import Blueprint, render_template, request, url_for, redirect, session
import pymongo, json, bcrypt
from database import db_get_resources

manage_routes = Blueprint('manage', __name__)

with open("config.json") as jsonfile:
    conf = json.load(jsonfile)

@manage_routes.route('/my')
def my():
    if "email" in session:
        email = session["email"]
        resources = db_get_resources.find(email=email)
        pkg_cpu = conf["packages"]["default"]["cpu"]
        pkg_ram = conf["packages"]["default"]["ram"]
        pkg_disk = conf["packages"]["default"]["disk"]
        pkg_servers = conf["packages"]["default"]["servers"]
        pkg_backups = conf["packages"]["default"]["backups"]
        pkg_databases = conf["packages"]["default"]["databases"]
        pkg_ports = conf["packages"]["default"]["ports"]
        add_cpu = resources["cpu"]
        add_ram = resources["ram"]
        add_disk = resources["disk"]
        add_servers = resources["servers"]
        add_backups = resources["backups"]
        add_databases = resources["databases"]
        add_ports = resources["ports"]
        cpu = pkg_cpu + add_cpu
        ram = pkg_ram + add_ram
        disk = pkg_disk + add_disk
        servers = pkg_servers + add_servers
        backups = pkg_backups + add_backups
        databases = pkg_databases + add_databases
        ports = pkg_ports + add_ports
        return render_template('my.html', email=email, cpu=cpu, ram=ram, 
                               disk=disk, servers=servers, backups=backups, 
                               databases=databases, ports=ports)
    else:
        return redirect(url_for("auth.login")) 