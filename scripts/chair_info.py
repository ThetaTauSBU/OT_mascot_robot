#!/usr/bin/python3

""" Retrieves brother chair information

boto library is required to be installed prior to usage and development.
"""
import boto3
import sys

s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)

TABLE_NAME = "Brothers"
REGION_NAME = "us-east-2"

# Creating the DynaoDB Client
dynamodb_client = boto3.client('dynamodb', region_name=REGION_NAME)

# Creating the DynamoDB Table Resource
dynamodb = boto3.resource('dynamodb', region_name=REGION_NAME)
table = dynamodb.Table(TABLE_NAME)


# Use table get item method to get a single item
resp = table.get_item(
    TableName=TABLE_NAME,
    Key={
        'Active': True,
        'Chair': sys.argv
    }
)

print(resp['Item'])
