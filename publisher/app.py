import json
import os
import time

import boto3

TOPIC_ARN = os.environ["TOPIC_ARN"]
SNS = boto3.client('sns')


def lambda_handler(event, context):
    begin_ts = time.time()
    print(f"Publishing at {begin_ts}")
    response = SNS.publish(
        TopicArn=TOPIC_ARN,
        Message=str(begin_ts)
    )
    end_ts = time.time()
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "Begin": str(begin_ts),
                "End": str(end_ts),
                "MessageId": response["MessageId"]
            }
        ),
    }
