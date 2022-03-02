import boto3
import sys

aws_mng_con = boto3.session.Session(profile_name="default")
ec2_con_re = aws_mng_con.resource(service_name="ec2", region_name="us-east-1")
ec2_con_cli = aws_mng_con.client(service_name="ec2", region_name="us-east-1")

while True:
    print("This script performs the following actions on EC2 instance")
    print(
        """
        1. start
        2. stop
        3. terminate
        4. exit
    """
    )
    opt = int(input("Enter your option: "))
    if opt == 1:
        instance_id = input("Enter your EC2 Instance Id: ")
        print("Starting EC2 instance....")
    elif opt == 2:
        instance_id = input("Enter your EC2 Instance Id: ")
        print("Stopping EC2 instance....")
    elif opt == 3:
        instance_id = input("Enter your EC2 Instance Id: ")
        print("Terminating EC2 instance....")
    elif opt == 4:
        sys.exit()
    else:
        print("Your option is invalid. Please try again!")
