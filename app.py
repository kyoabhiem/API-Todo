from flask import Flask
from importlib import import_module


def create_app():
    flaskApp = Flask(__name__, static_url_path="", static_folder="../public")
    module = import_module('{}.routes'.format('todo'))
    flaskApp.register_blueprint(module.blueprint)
    return flaskApp


if __name__ == '__main__':
    create_app().run(debug=True)
