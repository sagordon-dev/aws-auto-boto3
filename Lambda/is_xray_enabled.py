import boto3

# Generate a list of all lambdas that do not have the x-ray component enabled.
xray_disabled = []
xray_enabled = []

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
    print("Saving functions with X-Ray disabled to 'disabled_xray.txt'")
    with open("disabled_xray.txt", "w") as f:
        for item in xray_disabled:
            f.write(f"{item}\n")

# Based upon that report if there are lambdas that do not have x-ray enabled
# then a task will need to be created to enable x-ray
for item in xray_disabled:
    response = client.update_function_configuration(
        FunctionName=item, TracingConfig={"Mode": "Active"}
    )
    # TODO Generate listing with account name, lambda and x-ray enabled
    xray_enabled.append(item)

print(f"Enabled X-Ray on these Lambda functions: {xray_enabled}")

# TODO Save script into a rep like bwp-cds-common for reuse.
