from os import path
from flask import Flask

from .config.db import db, DB_NAME
from .routes import routes


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Database initialization
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Adding routes
    app.register_blueprint(routes, url_prefix="/")

    create_database(app)

    return app


def create_database(app):
    if not path.exists('app/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print("Database created")
