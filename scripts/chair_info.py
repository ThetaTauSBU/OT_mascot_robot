#!/usr/bin/python3

""" Retrieves brother chair information

boto library is required to be installed prior to usage and development.
"""
import boto3
from boto3.dynamodb.conditions import Key, Attr
import sys

if len(sys.argv) != 2:
    print('Missing chair position argument...')
    sys.exit(1)

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

resp = table.scan(
    FilterExpression=Attr('Chair').contains(sys.argv[1])
)

print(resp['Items'])

