import boto3

# AWS Region (Change if needed)
REGION = "ap-south-1"  # Mumbai Region

# Your EC2 Instance ID
INSTANCE_ID = "i-0c5cc1b8bbccc904b"

def lambda_handler(event, context):
    ec2 = boto3.client("ec2", region_name=REGION)
    
    # Get action from the event payload
    ACTION = event.get("ACTION", "").upper()

    if ACTION == "START":
        ec2.start_instances(InstanceIds=[INSTANCE_ID])
        return f"EC2 instance {INSTANCE_ID} started successfully."
    
    elif ACTION == "STOP":
        ec2.stop_instances(InstanceIds=[INSTANCE_ID])
        return f"EC2 instance {INSTANCE_ID} stopped successfully."
    
    else:
        return "Invalid action. Use 'START' or 'STOP'."
