def lambda_handler(event, context):
    """
    Minimal AWS Lambda handler. Returns a 200 response with a greeting.
    """
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": "Hello from Lambda!"
    }

