import boto3
import sys



s3_client = boto3.client("s3")
responce = s3_client.list_buckets()

client = boto3.client('ec2')

custom_filter = [{
    'Name':'tag:Owner', 
    'Values': ['user@example.com']}]
    
response = client.describe_instances(Filters=custom_filter)


print(response)
def s3_bucket():
    for bucket in s3_client.list_buckets()["Buckets"]:
        print(bucket["Name"])