from flask_sqlalchemy import SQLAlchemy
from backend.config import get_config

db = SQLAlchemy()

def init_db(app):
    """Initialize database with Flask app"""
    config_class = get_config()
    app.config.from_object(config_class)
    db.init_app(app)
