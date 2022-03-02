from urllib import response
import boto3
from pprint import pprint

aws_mng_con = boto3.session.Session(profile_name="default")
ec2_con_cli = aws_mng_con.client(service_name="ec2", region_name="us-east-1")

response = ec2_con_cli.describe_instances()["Reservations"]
for item in response:
    for instance in item["Instances"]:
        print("-----------------------------------------")
        print(
            f"The Image Id is: {instance['ImageId']}\nThe Instance Id is: {instance['InstanceId']}\nThe Instance Launch Time is: {instance['LaunchTime']}"
        )

response = ec2_con_cli.describe_volumes()["Volumes"]
for item in response:
    print("-----------------------------------------")
    print(
        f"The volume Id is: {item['VolumeId']}\nThe Availability Zone is: {item['AvailabilityZone']}\nThe Volume Type is: {item['VolumeType']}"
    )
