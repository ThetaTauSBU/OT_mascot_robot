#!/usr/bin/python3
import boto3
from boto3.dynamodb.conditions import Key, Attr
import sys

if len(sys.argv) <= 2:
    print('Missing date and time arguments.')
    sys.exit(1)

s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)

TABLE_NAME = "Events"
REGION_NAME = "us-east-2"

# Creating the DynamoDB Client
dynamodb_client = boto3.client('dynamodb', region_name=REGION_NAME)

# Creating the DynamoDB Table Resource
dynamodb = boto3.resource('dynamodb', region_name=REGION_NAME)
table = dynamodb.Table(TABLE_NAME)

resp = table.scan(
    FilterExpression=Attr('Date').contains(sys.argv[1]) & Attr('Time').gte(sys.argv[2])
)

resp2 = table.scan(
    FilterExpression = Attr('Date').gt(sys.argv[1])
)

minNum = 100 # largest number of events

if not resp['Items']:
    for item in resp2['Items']:
        if item['Number'] < minNum:
            minNum = item['Number']
            nextEvent = item
    print("The next event is " + nextEvent["EventName"] + " on " + nextEvent["Date"] + " at " + nextEvent["Time"] + "!")
else:
    print("The next event is " + resp['Items'][0]["EventName"] + " on " + resp['Items'][0]["Date"] + " at " + resp['Items'][0]["Time"] + "!")
