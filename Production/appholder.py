from flask import Flask
from flask_mongoengine import MongoEngine
from pymongo import MongoClient

import config
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from celery.task.schedules import crontab
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from celery import Celery
import redis
app = Flask(__name__)
app.config.from_pyfile('thisapp.cfg')
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['MONGODB_DB'] = config.MONGO_DB
db = SQLAlchemy(app)
ma = Marshmallow(app)
mo = MongoEngine(app)

client = MongoClient(host='0.0.0.0', port=27017)
# adding new value for db.session
db_session = db.session