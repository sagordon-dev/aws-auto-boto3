import boto3

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue. This returns an SQS.Queue instance
queue = sqs.get_queue_by_name(QueueName='test')

# You can now access identifiers and modifiers
print(queue.url)
print(queue.attributes.get('DelaySeconds'))

# Also possible to list all existing queues;
for queue in sqs.queues.all():
    print(queue.url)