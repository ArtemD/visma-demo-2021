from flask import Flask

#Another comment goes here :)
# this is my version!

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world!"

@app.route('/test')
def test():
    return "This is a test"
