import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'My_super_secret_key')
    DEBUG = os.getenv('FLASK_DEBUG', 'True').lower() in ['true', '1', 'yes']
    
    DATABASE_URL = os.getenv('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
        'pool_recycle': 300,
    }
    
    JWT_SECRET = os.getenv('JWT_SECRET', 'EXTRA_SECRET_JWT_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'EXTRA_SECRET_KEY')
    JWT_EXP_DELTA_SECONDS = int(os.getenv('JWT_EXP_DELTA_SECONDS', 3600)) * 24 * 30  # Default to 30 days
    JWT_ALGORITHM = 'HS256'
    
class DevelopmentConfig(Config):
    """Development configuration"""

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 
                                       'mysql+pymysql://hobby_user:hobby_password@mariadb:3306/hobby_db')

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    # changes these values for production
    SECRET_KEY = os.getenv('SECRET_KEY', "secret_key")
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', "jwt_secret_key")
    SESSION_COOKIE_SECURE = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    
    if not SECRET_KEY or not JWT_SECRET_KEY:
        raise ValueError("SECRET_KEY and JWT_SECRET_KEY must be set in production")


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}


def get_config():
    """Get configuration based on environment"""
    env = os.getenv('FLASK_ENV', 'development')
    return config.get(env, config['default'])
