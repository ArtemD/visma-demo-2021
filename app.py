from flask import Flask

#Comment goes here :)

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world! "
