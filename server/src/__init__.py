from flask import Flask
from flask_migrate import Migrate
from src.models import db
from src.config.config import DevelopmentConfig
from src.doctors import doctors_bp
from src.healthPrograms import health_programs_bp
from src.severity import severity_bp
from src.patients import patients_bp


migrate = Migrate()


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/')
    def hello_world():
        return 'Welcome to the Health Management System API!'

    # Register blueprints
    app.register_blueprint(doctors_bp, url_prefix='/api/v1/doctors')
    app.register_blueprint(health_programs_bp, url_prefix='/api/v1/programs')
    app.register_blueprint(severity_bp, url_prefix='/api/v1/severity')
    app.register_blueprint(patients_bp, url_prefix='/api/v1/patients')

    return app
