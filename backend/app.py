import time
from flask import Flask, render_template, jsonify
from random import *

def create_app():
    app = Flask(__name__,
                static_folder= "../dist/static",
                # this is in sort, adding it to the path except facilitating to the backend only yay
                template_folder="../dist")
    return app

app = create_app()

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
    return render_template("index.html")




