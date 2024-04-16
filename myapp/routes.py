from flask import render_template
from myapp import myappFlaskInstance

@myappFlaskInstance.route('/')
@myappFlaskInstance.route('/index')
def index():
    user = {'username': 'Peter'}
    return render_template('index.html', title='Home', user=user)