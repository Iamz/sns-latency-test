import json
import time


def lambda_handler(event, context):
    ts = time.time()
    message_id = event["Records"][0]["Sns"]["MessageId"]
    message = event["Records"][0]["Sns"]["Message"]
    print(json.dumps({
        "Received": str(ts),
        "MessageId": message_id,
        "Message": message
    }))
