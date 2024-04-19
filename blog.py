import sqlalchemy as sa
import sqlalchemy.orm as so
from myapp import myappFlaskInstance, db
from myapp.models import User, Post

@myappFlaskInstance.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post}