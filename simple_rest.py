"""Some Comment"""
from flask import Flask
APP = Flask(__name__)


@APP.route('/greet')
def say_hello():
    """Some Comment"""
    return 'Greetings from Flask Server'

@APP.route('/')
def index():
    """Some Comment"""
    return 'Home Page'

@APP.route('/hello')
def hello():
    """Some Comment"""
    return 'Hello, greetings from different endpoint'

#adding variables
@APP.route('/hello/<username>')
def show_user(username):
    """Some Comment"""
    return 'Welcome: %s' % username

@APP.route('/post/<int:post_id>')
def show_post(post_id):
    """returns the post, the post_id should be an int"""
    return str(post_id)

if __name__ == '__main__':
    APP.run(debug=False)
