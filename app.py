from flask import Flask
from importlib import import_module


def create_app():
    flask_app = Flask(__name__, static_url_path="", static_folder="../public")
    module = import_module('{}.routes'.format('todo'))
    flask_app.register_blueprint(module.blueprint)
    return flask_app


if __name__ == '__main__':
    create_app().run(debug=True)
