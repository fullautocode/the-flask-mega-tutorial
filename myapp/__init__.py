from flask import Flask

myappFlaskInstance = Flask(__name__)

from myapp import routes 
