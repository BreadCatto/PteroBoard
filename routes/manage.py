from flask import Blueprint, render_template, request, url_for, redirect, session
import pymongo, json, bcrypt
from database import db_create_user
from app import create_user

manage_routes = Blueprint('manage', __name__)
@manage_routes.route('/my')


def my():
    if "email" in session:
        email = session["email"]
        return render_template('my.html', email=email)
    else:
        return redirect(url_for("auth.login")) 