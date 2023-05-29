from flask import Blueprint, render_template, request, url_for, redirect, session
import pymongo, json, bcrypt
from database import db_create_user
from app import create_user

auth_routes = Blueprint('auth', __name__)
with open("config.json") as jsonfile:
    conf = json.load(jsonfile)

client = pymongo.MongoClient(conf["app"]["mongodb_url"])
db = client.get_database('pteroclient')
records = db.users


@auth_routes.route("/", methods=["POST", "GET"])
async def login():
    message = 'Please login to your account'
    if "email" in session:
        return redirect(url_for("manage.my"))
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        email_found = records.find_one({"email": email})
        if email_found:
            email_val = email_found['email']
            passwordcheck = email_found['password']
            if bcrypt.checkpw(password.encode('utf-8'), passwordcheck):
                session["email"] = email_val
                return redirect(url_for('manage.my'))
            else:
                if "email" in session:
                    return redirect(url_for("manage.my"))
                message = 'Wrong password'
                return render_template('login.html', message=message)
        else:
            message = 'Email not found'
            return render_template('login.html', message=message)
    return render_template('login.html', message=message)

@auth_routes.route("/register", methods=['POST', 'GET'])
async def register():
    message = 'Please Register your account.'
    if "email" in session:
        return redirect(url_for("manage.my"))
    if request.method == "POST":
        user = request.form.get("fullname")
        email = request.form.get("email")
        password = request.form.get("password")
        user_found = records.find_one({"name": user})
        email_found = records.find_one({"email": email})
        username_check = create_user.username_check(username=user)
        email_check = create_user.email_check(email=email)
        if username_check == "exist":
            message = 'There already is a user by that name.'
            return render_template('register.html', message=message)
        if email_check == "exist":
            message = 'This email already exists in database.'
            return render_template('register.html', message=message)
        if user_found:
            message = 'There already is a user by that name.'
            return render_template('register.html', message=message)
        if email_found:
            message = 'This email already exists in database.'
            return render_template('register.html', message=message)
        else:
            hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            ptero_id = create_user.create(email=email, username=user, password=password)
            if ptero_id == "error":
                message = "an error occured"
                print(message)
                return render_template('register.html', message=message)
            else:
                db_create_user.create(email=email, password=hashed, username=user, pteroid=ptero_id)
                user_data = records.find_one({"email": email})
                new_email = user_data['email']
                return redirect(url_for("manage.my"))
    return render_template('register.html', message=message)
  

@auth_routes.route("/logout", methods=["POST", "GET"])
async def logout():
    if "email" in session:
        session.pop("email", None)
        return redirect(url_for("auth.login"))
    else:
        return render_template('login.html')
    