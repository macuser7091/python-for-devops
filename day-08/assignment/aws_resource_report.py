import boto3
import sys



s3_client = boto3.client("s3")
responce = s3_client.list_buckets()

# ec2_client = boto3.client("ec2")
client = boto3.client('ec2')

custom_filter = [{
    'Name':'tag:Owner', 
    'Values': ['user@example.com']}]
    
response = client.describe_instances(Filters=custom_filter)

# response = client.describe_tags(

# ec2_responce = ec2_client.describe_instances()
# print(type(ec2_responce))

print(response)
def s3_bucket():
    for bucket in s3_client.list_buckets()["Buckets"]:
        print(bucket["Name"])