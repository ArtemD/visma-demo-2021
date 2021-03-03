import threading
from flask import Flask, request
from logme import logger
from api import get_json

app = Flask(__name__)
""" This is an app variable """

@app.route('/api/v1/all')
def api():
    """
    Get all licenses and output as JSON
    """
    logger.debug('Got request for API/ALL from %s' % request.remote_addr)
    return get_json()

if __name__ == '__main__':
    app.config['DEBUG']=True
    """ Set debug mode on for local development """
    app.run(threaded=False, port=5000)
    """ Run flask in local development mode on port 5000 """