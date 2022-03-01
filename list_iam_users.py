import boto3

aws_mgmnt_cons = boto3.session.Session(profile_name="boto3_user")
iam_con = aws_mgmnt_cons.resource("iam")

# iam_con = boto3.resource(service_name="iam", region_name="us-east-1")

for each_user in iam_con.users.all():
    print(each_user.name)
