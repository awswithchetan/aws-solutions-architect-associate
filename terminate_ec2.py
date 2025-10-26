import boto3

# Ask user for region and instance ID
region = input("Enter AWS region code (e.g.ap-south-1 or us-east-1): ").strip()
instance_id = input("Enter the EC2 Instance ID to terminate (e.g., i-0abcd123456789xyz): ").strip()

# Create EC2 client for the selected region
ec2 = boto3.client('ec2', region_name=region)

try:
    # Terminate the instance
    response = ec2.terminate_instances(
        InstanceIds=[instance_id]
    )

    print(f"\nTermination initiated successfully!")
    print(f"Region: {region}")
    print(f"Instance ID: {instance_id}")

except Exception as e:
    print(f"\nFailed to terminate instance {instance_id} in {region}: {e}")
