from flask import Flask, request, render_template
from logme import logger
from api import get_json, get_by_id

app = Flask(__name__)
""" This is an app variable """

@app.route('/')
def index():
    return render_template('front-page.html')

@app.route('/api/v1/all')
def api():
    """
    Get all licenses and output as JSON
    """
    logger.debug('Got request for API/ALL from %s' % request.remote_addr)
    return get_json()

@app.route('/api/v1/search/')
@app.route('/api/v1/search/<id>')
def api_search_by_id(id=None):
    """
    Search for license by id or return 404 if not found

    Parameters
    ----------
    id: str
        Id of the license row
    """
    return get_by_id(id)

if __name__ == '__main__':
    app.config['DEBUG']=True
    """ Set debug mode on for local development """
    app.run(threaded=False, port=5000)
    """ Run flask in local development mode on port 5000 """