import boto3

aws_mgmnt_cons = boto3.session.Session(profile_name="boto3_user")
s3_cons = aws_mgmnt_cons.resource("s3")

for each_bucket in s3_cons.buckets.all():
    print(each_bucket.name)
