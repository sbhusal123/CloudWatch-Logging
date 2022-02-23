# pip install watchtower
# Documentation: https://pypi.org/project/watchtower/

# Please visit the documentation 

from cmath import log
import watchtower, logging

import os

from dotenv import load_dotenv

# Load from .env file
try:
	load_dotenv()
except Exception as e:
	pass



# These are the environment variables to be used by Boto3
# Tells where to push those logs to.
os.environ["AWS_ACCESS_KEY_ID"]  = os.getenv("AWS_ACCESS_KEY_ID")
os.environ["AWS_SECRET_ACCESS_KEY"] = os.getenv("AWS_SECRET_ACCESS_KEY")
os.environ["AWS_DEFAULT_REGION"] = os.getenv("AWS_DEFAULT_REGION")



logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# WatchTower Log Handler
handler = watchtower.CloudWatchLogHandler(log_group_name="WatchTowerLog")
logger.addHandler(handler)

# logging message
logger.error("This is a test")