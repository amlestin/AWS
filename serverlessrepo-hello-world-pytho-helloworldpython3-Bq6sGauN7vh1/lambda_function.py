import json

print('Weekend function')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    print("First = " + event['key1'])
    print("Second = " + event['key2'])
    print("Third = " + event['key3'])
    return event['key1']  # Echo back the first key value
    #raise Exception('Something went wrong')
