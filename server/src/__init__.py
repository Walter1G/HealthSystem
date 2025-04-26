# src/__init__.py

from flask import Flask
from flask_migrate import Migrate
from src.models import db
from src.config.config import DevelopmentConfig

migrate = Migrate()

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/')
    def hello_world():
        return 'Welcome to the Health Management System API!'

    return app
