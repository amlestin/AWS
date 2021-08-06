import json
from botocore.vendored import requests
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def lambda_handler(event, context):
    route = int(event)
    # input validation
    if route < 0:
        return "Invalid Input"

    response = requests.get(F'https://www.usfbullrunner.com/Route/{route}/')

    posts = json.loads(response.text)
    return posts