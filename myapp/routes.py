from myapp import myappFlaskInstance

@myappFlaskInstance.route('/')
@myappFlaskInstance.route('/index')
def index():
    return "Hello, World!"
