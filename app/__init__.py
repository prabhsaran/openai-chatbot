from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os

from .routes import routes

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Simple Secret Key"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Database initialization
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Adding routes
    app.register_blueprint(routes, url_prefix="/")

    create_database(app)

    return app


def create_database(app):
    print(os.getcwd())
    if not path.exists('app/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print("Database created")
