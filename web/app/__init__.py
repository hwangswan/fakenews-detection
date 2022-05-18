'''Init Flask app'''

import os

from flask import Flask, render_template
from flask_restful import Api

from .modules.detection import Detection
from .modules.pipeline import Pipeline

def create_app(test_config = None):
    '''Create a Flask app'''

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
    api.add_resource(Detection, '/detect', endpoint = 'detect')

    @app.route('/')
    def index():
        try:
            classifiers_list = Pipeline().get_classifiers_list()
        except FileNotFoundError as file_error:
            return render_template('html/404.html', message = str(file_error))

        return render_template('html/index.html', classifiers_list = classifiers_list)

    @app.route('/index_js')
    def index_js():
        return render_template('js/index.js')

    return app
