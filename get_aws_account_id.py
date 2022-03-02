import boto3

aws_mng_con = boto3.session.Session(profile_name="default")
sts_con_cli = aws_mng_con.client(service_name="sts", region_name="us-east-1")
response = sts_con_cli.get_caller_identity()
print(response["Account"])
