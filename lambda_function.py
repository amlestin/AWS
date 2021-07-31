import json
from botocore.vendored import requests
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
def lambda_handler(event, context):
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = json.loads(response.text) #load data into a dict of objects, posts
    print(posts)