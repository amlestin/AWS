import json
from botocore.vendored import requests
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def lambda_handler(event, context):
    route = int(event)
    response = requests.get(F'https://www.usfbullrunner.com/Route/{route}/')

    posts = json.loads(response.text)
    return posts