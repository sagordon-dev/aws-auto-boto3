import boto3

aws_mng_con = boto3.session.Session(profile_name="default")
iam_con_re = aws_mng_con.resource(service_name="iam",region_name="us-east-1")
ec2_con_re= aws_mng_con.resource(service_name="ec2",region_name="us-east-1")
s3_con_re = aws_mng_con.resource(service_name="s3",region_name="us-east-1")

for user in iam_con_re.users.all():
    print(user.user_name)