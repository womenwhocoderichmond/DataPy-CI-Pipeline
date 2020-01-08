from flask import Flask
app = Flask(__name__)


@app.route('/greet')
def say_hello():
  return 'Greetings from Flask Server'

@app.route('/')
def index():
  return 'Home Page'

@app.route('/hello')
def hello():
  return 'Hello, greetings from different endpoint'

#adding variables
@app.route('/hello/<username>')
def show_user(username):
  #returns the username
  return 'Welcome: %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
  #returns the post, the post_id should be an int
  return str(post_id)

if __name__ == '__main__':
    app.run(debug=False)
    
