import boto3

aws_mag_con_root = boto3.session.Session(profile_name="boto3_user")

iam_con_re = aws_mag_con_root.resource(service_name="iam", region_name="us-east-1")
iam_con_cli = aws_mag_con_root.client(service_name="iam", region_name="us-east-1")

# Listing iam users with resource object:

for each_user in iam_con_re.users.all():
    print(each_user.name)

print("---------------------------------------")

# LIsting iam ursers with client:

for each in iam_con_cli.list_users()["Users"]:
    print(each["UserName"])
