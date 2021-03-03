import logging
import os
from dotenv import load_dotenv
load_dotenv()

LOG_DIR = os.environ['LOG_DIR']

if os.path.exists(LOG_DIR)==False:
    os.makedirs(LOG_DIR)

logger = logging.getLogger('api')
fh = logging.FileHandler('%s/api.log' % LOG_DIR)
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(funcName)s:%(lineno)d %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)