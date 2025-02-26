

Readme
AWS EC2 Scheduler (Auto Start/Stop EC2)
🚀 Overview
This project automates the starting and stopping of an AWS EC2 instance on a schedule using AWS Lambda and Amazon EventBridge (CloudWatch Events). This helps reduce costs by running instances only when needed.

📌 Features
✅ Automatically starts an EC2 instance at 9 AM and stops it at 6 PM ✅ Uses AWS Lambda to execute the start/stop actions ✅ Uses Amazon EventBridge to trigger Lambda on a schedule ✅ IAM Role permissions to allow Lambda to control EC2 ✅ Fully serverless, no manual intervention required

🏗️ AWS Services Used
Service	Purpose
EC2	Virtual Machine that needs to be scheduled
Lambda	Python script that starts/stops EC2 instance
EventBridge (CloudWatch Events)	Schedules Lambda execution
IAM	Permissions for Lambda to control EC2
CloudWatch Logs	Logs function execution & errors
📁 Folder Structure
AWS-EC2-Scheduler/
│── lambda_code/
│   ├── lambda_function.py   # AWS Lambda script
│
│── screenshots/
│   ├── setup_1.png   # Screenshots of AWS setup
│   ├── setup_2.png
│
│── documentation/
│   ├── setup.md   # Step-by-step guide
│
│── README.md  # Project Documentation
⚙️ Setup Guide
1️⃣ Create an EC2 Instance
Go to AWS EC2 Dashboard → Click Launch Instance

Choose an Amazon Machine Image (AMI) (e.g., Amazon Linux 2023)

Choose an Instance Type (Free Tier: t2.micro)

Configure security group to allow SSH (port 22)

Create & download a Key Pair (for SSH access)

Click Launch and note the Instance ID

2️⃣ Create an IAM Role for Lambda
Go to IAM Console → Roles → Create Role

Choose AWS Service → Lambda

Attach the AmazonEC2FullAccess policy (or create a custom policy with start/stop permissions)

Name the role LambdaEC2SchedulerRole and save it

3️⃣ Create a Lambda Function
Go to AWS Lambda → Create Function

Select "Author from Scratch"

Runtime: Python 3.x

Execution Role: Choose LambdaEC2SchedulerRole


4️⃣ Set Up Amazon EventBridge (CloudWatch Events)
Go to Amazon EventBridge → Rules → Create Rule

Rule Name: EC2StartSchedulerRule

Schedule: 0 3 * * ? * (9 AM IST, UTC time)

Select Target: Lambda Function → Choose your Lambda function

Add Constant Input: { "ACTION": "START" }

Click Create

Repeat the above for the Stop Rule:

Rule Name: EC2StopSchedulerRule

Schedule: 0 12 * * ? * (6 PM IST, UTC time)

Constant Input: { "ACTION": "STOP" }

🚀 Testing Your Lambda Function
You can test the Lambda function manually:

Start EC2 Test Event
{
  "ACTION": "START"
}
Stop EC2 Test Event
{
  "ACTION": "STOP"
}
Run the test in AWS Lambda → Test and check if the EC2 instance starts/stops.

🛠️ Troubleshooting
🔹 Lambda Times Out? → Increase the timeout to 30 seconds in Lambda settings 🔹 Instance Not Starting? → Check if IAM Role has correct permissions 🔹 EventBridge Not Triggering? → Check CloudWatch Logs for errors

🎯 Future Enhancements
🔹 Start/Stop multiple EC2 instances using Tags instead of IDs 🔹 Web Interface (AWS API Gateway + Lambda) to trigger actions manually 🔹 Slack/Email Notifications when instance starts/stops

