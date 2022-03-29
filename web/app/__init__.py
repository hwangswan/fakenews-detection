import os

from flask import Flask, render_template
from flask_restful import Api

from .modules.Detection import Detection

def create_app(test_config = None):
    app = Flask(__name__, instance_relative_config = True)
    
    app.config.from_mapping(
        SECRET_KEY='1337'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent = True)
    else:
        app.config.from_mapping(test_config)


    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    api = Api(app)
    api.add_resource(Detection, '/detect')

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
