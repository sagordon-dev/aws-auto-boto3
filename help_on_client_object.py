import boto3

aws_mng_con = boto3.session.Session(profile_name="boto3_user")

# Create IAM, EC2, and S3
iam_con_cli = aws_mng_con.client(service_name="iam", region_name="us-east-1")
ec2_con_cli = aws_mng_con.client(service_name="ec2", region_name="us-east-1")
s3_con_cli = aws_mng_con.client(service_name="s3", region_name="us-east-1")

# List all IAM users with client objects
print("----------------------IAM Users------------------------")
response = iam_con_cli.list_users()
for each_user in response["Users"]:
    print(each_user["UserName"])

# List all EC2 instance IDs
print("----------------------EC2 Instances-------------------------")
response = ec2_con_cli.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        print(instance["InstanceId"])

# List all S3 Bucket Names
print("---------------------S3 Bucket Names------------------------")
response = s3_con_cli.list_buckets()
for bucket in response["Buckets"]:
    print(bucket["Name"])
