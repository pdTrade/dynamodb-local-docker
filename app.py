import boto3

dynamodb = boto3.resource(
  'dynamodb',
  endpoint_url="http://localhost:8000",
  region_name='us-west-2',
  aws_access_key_id='ACCESSID',
  aws_secret_access_key='ACCESSKEY'
)

table = dynamodb.create_table(
  TableName='customers',
  AttributeDefinitions=[
    {
      'AttributeName': 'customer_id',
      'AttributeType': 'S'
    },
    {
      'AttributeName': 'order_id',
      'AttributeType': 'S'
    },
  ],
  KeySchema=[
    {
      'AttributeName': 'customer_id',
      'KeyType': 'HASH'
    },
    {
      'AttributeName': 'order_id',
      'KeyType': 'RANGE'
    },
  ],
  ProvisionedThroughput={
    'ReadCapacityUnits': 5,
    'WriteCapacityUnits': 5,
  },
)

print('Table status:', table.table_status)

