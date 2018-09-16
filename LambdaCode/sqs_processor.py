import boto3
region = 'us-east-1'

queue_url = 'https://sqs.us-east-1.amazonaws.com/812225150599/arcade-sqs-queue'

sqs = boto3.resource('sqs', region_name=region)

# Lambda execution starts here
def handler(event, context):

  queue = sqs.get_queue_by_name(QueueName='arcade-sqs-queue')
  messages = queue.receive_messages()
  for message in messages:
    print('Body: {0}'.format(message.body))
    message.delete()
