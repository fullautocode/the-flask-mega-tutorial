from flask import render_template
from myapp import myappFlaskInstance
from myapp.forms import LoginForm

@myappFlaskInstance.route('/')
@myappFlaskInstance.route('/index')
def index():
    user = {'username': 'Peter'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@myappFlaskInstance.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)