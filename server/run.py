# run.py
from src import create_app
from src.config.config import DevelopmentConfig, TestingConfig, ProductionConfig
import os

env = os.environ.get('FLASK_ENV', 'development')

if env == 'development':
    app = create_app(DevelopmentConfig)
elif env == 'testing':
    app = create_app(TestingConfig)
elif env == 'production':
    app = create_app(ProductionConfig)
else:
    app = create_app(DevelopmentConfig)

if __name__ == "__main__":
    app.run()
