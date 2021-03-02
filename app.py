from flask import Flask

#Csdjfgh sdfjh jkhdfgsdkajhfgdakjsdfdsfdsfsdfsdf sfd sdf sdfs dfs dfhg fkajehgf kjhwegf kjhwegkjhfg wekjhgf knt goes here :)
#Another comment goes here :)

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world! "
