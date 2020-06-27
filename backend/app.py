import time
from flask import Flask
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)
    load_dotenv()

    @app.route('/')
    def index():
        return '<h1> This one is for all my frisbee bois </h1>'

    @app.route('/time')
    def get_current_time():
        return {'time': time.time()}

    return app
