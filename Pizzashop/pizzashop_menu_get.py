import boto3
from boto3 import dynamodb 
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    table = boto3.resource('dynamodb', region_name='us-west-2').Table('Menu')
    item = table.get_item(Key={'menu_id': event['menu_id']}).get('Item')
    return {
        "statusCode": 200,
        "headers": { "Content-Type": "application/json"},
        "body": item
    }