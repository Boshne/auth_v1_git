"""
Store configuration
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.163.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '25'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    if not (MAIL_USERNAME and MAIL_PASSWORD):
        raise ValueError("MAIL USERNAME OR PASSWORD HAS NOT BEEN WRITEN TO ENV VARIABLES.")
    # MAIL_USERNAME = '18637772876@163.com'
    # MAIL_PASSWORD = 'z326652929z'
    FLASKY_MAIL_SUBJECT_PREFIX = '[Customer Confirmation]'
    FLASKY_MAIL_SENDER = 'Fangling Admin <18637772876@163.com>'
    # FLASKY_ADMIN = os.environ.get('Fangling_Admin')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123@localhost/fangling'
    # COMMIT_ON_TEARDOWN: After each request, commit changes in database automatically.
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


class TestingConfig(Config):
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
    #     'sqlite://'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123@localhost/fangling'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


class ProductionConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123@localhost/fangling'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
