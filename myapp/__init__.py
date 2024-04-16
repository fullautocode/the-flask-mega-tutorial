from flask import Flask
from config import Config

myappFlaskInstance = Flask(__name__)
myappFlaskInstance.config.from_object(Config)

from myapp import routes