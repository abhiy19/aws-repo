import os
import json

def handler(event, context):
    version = os.environ.get("VERSION", "0.0")
    response_body = {
        "message": "Hello Abhinav from Devops",
        "version": version
    }

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(response_body)
    }
