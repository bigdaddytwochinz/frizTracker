import time
from flask import Flask, render_template, jsonify
from flask_cors import CORS
from random import *

def create_app():
    app = Flask(__name__,
                static_folder= "../dist/static",
                # this is in sort, adding it to the path except facilitating to
                # the backend only yay
                template_folder="../dist")

    cors = CORS(app, resources = {r"/api/*": {"origins": "*"}})

    return app, cors

app, cors = create_app()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/api/random')
def random_num():
    response = {
        'randomNumber': randint(1, 69)
    }
    return jsonify(response)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")
