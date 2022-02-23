> Reference repository for seting up cloud watch based logging with boto3 and AWS Cloud Watch and python.

## Logging With AWS Cloud Watch
- [WatchTower](https://pypi.org/project/watchtower/)


[Youtube: Complete Visibility of Your Cloud Resources and Applications](https://www.youtube.com/watch?v=a4dhoTQCyRA)


## 1. Setting up AWS CLI:

- **Install AWS CLI:** [Installation Steps Mentioned Here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

- **Get the required credentials:** ``AWS_ACCESS_KEY_ID`` ``AWS_SECRET_ACCESS_KEY`` ``AWS_DEFAULT_REGION``

- **Configure using:** ``aws configure`` with the above credentials

## 2. Using in Development: This repo is just a reference

- **Make sure you have installed the packages listed in requirements.txt**

- **Refer .env.sample in the repo.**

- **Add the environment variables from any source. ``[Recommended:] python-dot-env``**
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
    - AWS_DEFAULT_REGION

> These parameters are internally used by boto3 to call the AWS endpoints.

- **Setting up CLoudWatch Handler**

```python
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


# WatchTower Log Handler:
handler = watchtower.CloudWatchLogHandler(log_group_name="WatchTowerLog")
logger.addHandler(handler)

# logging message
logger.error("This is a test")
```

> For Other reference in setting up with Flask and Django please refer the watchtower documentation



## 3. How to Read the Logs:
- **To get the log from Specific group_name and stream:** ``bash get_logs``.
    - This requires you to pass the name of ``log_group`` and ``stream``.
- **To get the live lofs:** ``bash logs_tail``
    - This requires you to pass the name of ``log_group`` only


## 5. Author:
- **Surya Bhusal**