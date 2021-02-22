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

# sort active brothers by number
active_list = sorted(response['Items'], key = lambda i: i['Number'])

# Prints each element in response
for i in range(len(active_list)):
    print(str(i + 1) + ") #" + str(active_list[i]['Number']) + " " + str(active_list[i]['FirstName']) + " " + str(active_list[i]['LastName']))

