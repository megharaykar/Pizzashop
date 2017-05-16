import boto3
import json
from botocore.exceptions import ClientError

def lambda_handler(event, context):
  try:
    table = boto3.resource('dynamodb', region_name='us-west-2').Table('Menu')
    table.delete_item(Key={'menu_id': event['menu_id']})
    response = {}
    return response
  except Exception as e:
    return e.message