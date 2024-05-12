import os


class Config:
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DATABASE_URI = os.getenv('DATABASE_URI')


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEBUG = True


class LocalConfig(Config):
    DEBUG = True


app_config = {
    'local': LocalConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
