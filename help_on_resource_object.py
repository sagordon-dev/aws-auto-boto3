import boto3

aws_mng_con = boto3.session.Session(profile_name="default")

iam_con_re = aws_mng_con.resource(service_name="iam", region_name="us-east-1")
ec2_con_re = aws_mng_con.resource(service_name="ec2", region_name="us-east-1")
s3_con_re = aws_mng_con.resource(service_name="s3", region_name="us-east-1")

# List all IAM users
for user in iam_con_re.users.all():
    print(user.user_name)
# List only 2 users
for user in iam_con_re.users.limit(2):
    print(user.user_name)
print("--------------------------------------------------")
# List all S3 buckets
for bucket in s3_con_re.buckets.all():
    print(bucket)
# List all names on S3 buckets
for bucket in s3_con_re.buckets.all():
    print(bucket.name)
print("--------------------------------------------------")
# List all EC2 instance IDs
for instance in ec2_con_re.instances.all():
    print(instance.instance_id)
# List all EC2 instance architectures
for instance in ec2_con_re.instances.all():
    print(instance.architecture)
