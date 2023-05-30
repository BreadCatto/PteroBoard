from flask import Flask, render_template, request, url_for, redirect, session
import json
import os

with open("config.json") as jsonfile:
    conf = json.load(jsonfile)

app = Flask(__name__)
app.secret_key = "dsvcbdbxbbxccvxvxcvxcvxcvxcv"

for file in os.listdir('routes'):
    if file.endswith('.py') and file != '__init__.py':
        module_name = file[:-3]
        module = __import__(f'routes.{module_name}', fromlist=[module_name])
        blueprint = getattr(module, f'{module_name}_routes')
        app.register_blueprint(blueprint)

if __name__ == "__main__":
    app.run(debug=True, host=conf["app"]["host"], port=conf["app"]["port"])