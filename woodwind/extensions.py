from flask.ext.login import LoginManager
from flask.ext.micropub import MicropubClient
from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()
micropub = MicropubClient(client_id='redwind-reader')
login_mgr = LoginManager()
login_mgr.login_view = 'login'


def init_app(app):
    db.init_app(app)
    micropub.init_app(app)
    login_mgr.init_app(app)
