from flask import Flask

app = Flask(__name__)
""" This is an app variable """

@app.route('/')
def index():
    return "Hello world!"

@app.route('/test')
def test():
    """
    This is a great function
    """
    return "This is a test"
