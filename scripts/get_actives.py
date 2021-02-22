#!/usr/bin/python3

import boto3
from boto3.dynamodb.conditions import Key

s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)

TABLE_NAME = "Brothers"
REGION_NAME = "us-east-2"

# Creating the DynamoDB Client
dynamodb_client = boto3.client('dynamodb', region_name=REGION_NAME)

# Creating the DynamoDB Table Resource
dynamodb = boto3.resource('dynamodb', region_name=REGION_NAME)
table = dynamodb.Table(TABLE_NAME)

# Use table to retrieve all active brothers
response = table.scan(
    FilterExpression=Key('Active').eq(True)
)

# prints the number of active bros
print("There are " + str(len(response["Items"])) + " active brothers.")

