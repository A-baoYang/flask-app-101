from flask import Flask

from snakeeyes.blueprints.page import page


def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)  # slient=True: if the file does not exist, it will not raise an error

    app.register_blueprint(page)

    return app
