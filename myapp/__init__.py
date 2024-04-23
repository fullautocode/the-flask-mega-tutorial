from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

myappFlaskInstance = Flask(__name__)
myappFlaskInstance.config.from_object(Config)
db = SQLAlchemy(myappFlaskInstance)
migrate = Migrate(myappFlaskInstance, db)
login = LoginManager(myappFlaskInstance)

from myapp import routes, models 
