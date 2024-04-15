# EC2 Instance
resource "aws_instance" "data_processing_instance" {
  ami           = "your-ami-id" # Update with your AMI ID
  instance_type = "t2.micro"    # Update instance type as needed

  iam_instance_profile = aws_iam_role.ec2_role.name

  user_data = <<-EOF
              #!/bin/bash
              sudo yum update -y
              sudo yum install -y python3
              sudo pip3 install pandas snowflake-connector-python boto3
              EOF
}
