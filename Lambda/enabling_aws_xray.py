'''
    File name: enabling_aws_xray.py
    Author: Scott Gordon
    Date created: 3/2/2022
    Date last modified: 3/3/2022
    Python Version: 3.8
'''
import boto3

xray_disabled = []
xray_enabled = []

# Generate a list of all lambdas that do not have the x-ray component enabled.
client = boto3.client("lambda", region_name="us-east-1")
response = client.list_functions()

for item in response["Functions"]:
    if item["TracingConfig"]["Mode"] == "PassThrough":
        xray_disabled.append(item["FunctionName"])
    else:
        xray_enabled.append(item["FunctionName"])
if len(xray_disabled) == 0:
    print("There are no functions currently that have X-Ray disabled.")
else:
    print("These functions have X-Ray disabled.")
    print("Saving functions with X-Ray disabled to 'disabled_xray.txt'")
    with open("disabled_xray.txt", "w") as f:
        for item in xray_disabled:
            f.write(f"{item}\n")

# Enable X-Ray from xray_disabled list.
print(f"Enabling X-Ray on these Lambda functions: {xray_disabled}")
for item in xray_disabled:
    response = client.update_function_configuration(
        FunctionName=item, TracingConfig={"Mode": "Active"}
    )
    # Add newly enabled X-Ray items to xray_enabled list.
    print("Saving functions with X-Ray enabled to 'enabled_xray.txt'")
    xray_enabled.append(item)
    with open("enabled_xray.txt", "w") as f:
        for item in xray_disabled:
            f.write(f"{item}\n")
