import boto3

# Ask user for AWS region
region = input("Enter AWS region code (e.g.ap-south-1 or us-east-1): ").strip()

# Create clients for EC2 and SSM in the selected region
ssm = boto3.client('ssm', region_name=region)
ec2 = boto3.client('ec2', region_name=region)

# Get the latest Amazon Linux 2023 AMI ID dynamically from SSM Parameter Store
try:
    ami_param = ssm.get_parameter(
        Name="/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64"
    )
    ami_id = ami_param['Parameter']['Value']
    print(f"Found latest Amazon Linux 2023 AMI for {region}: {ami_id}")
except Exception as e:
    print(f"Failed to retrieve AMI for region {region}: {e}")
    exit(1)

# Launch the EC2 instance
response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType="t2.micro",
    MinCount=1,
    MaxCount=1,
    TagSpecifications=[
        {
            "ResourceType": "instance",
            "Tags": [{"Key": "Name", "Value": "AL3-NoKeyDemo"}]
        }
    ]
)

# Print instance details
instance_id = response["Instances"][0]["InstanceId"]
print("\nEC2 instance launched successfully!")
print(f"Region: {region}")
print(f"AMI ID: {ami_id}")
print(f"Instance ID: {instance_id}")
