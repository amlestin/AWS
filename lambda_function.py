import json

print('Make input text lowercase function')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    print("Lowercase text = " + event['key1'].lower())

    return event['key1']  # Echo back the first key value
    #raise Exception('Something went wrong')
