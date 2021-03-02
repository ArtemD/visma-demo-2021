from flask import Flask

#Csdjfgh sdfjh jkhdfgsdkajhfgdakjhg fkajehgf kjhwegf kjhwegkjhfg wekjdsfs fsdfsdf sdf wef wef sdf dsf sdf sdf sdf sdfhgf knt goes here :)
#Another comment goes here :)

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world! "
