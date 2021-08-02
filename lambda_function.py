import json
from botocore.vendored import requests
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def lambda_handler(event, context):
    response = requests.get('https://www.usfbullrunner.com/Route/13928/')

    posts = json.loads(response.text)
    print(posts)