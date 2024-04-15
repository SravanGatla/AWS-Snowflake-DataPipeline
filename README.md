# AWS-Snowflake-DataPipeline

## Data Processing Infrastructure on AWS

This repository contains the infrastructure code to set up a data processing environment on AWS. The infrastructure includes an EC2 instance for data processing, an S3 bucket for data storage, and CloudWatch Logs for monitoring.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Infrastructure Components](#infrastructure-components)
- [Setup Instructions](#setup-instructions)
- [Dockerization](#dockerization)
- [Jenkins CI/CD Pipeline](#jenkins-cicd-pipeline)
- [Terraform Automation](#terraform-automation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before setting up the infrastructure, make sure you have the following:

- AWS Account
- AWS CLI installed and configured
- Docker installed
- Jenkins installed and configured

## Infrastructure Components

### 1. EC2 Instance

An EC2 instance is provisioned to handle data processing tasks.

- **AMI**: Amazon Machine Image (Replace `your-ami-id` with the desired AMI ID)
- **Instance Type**: `t2.micro`

### 2. S3 Bucket

An S3 bucket is created to store data files securely.

- **Bucket Name**: `your-s3-bucket-name`

### 3. CloudWatch Logs

CloudWatch Logs are configured to monitor the EC2 instance logs.

- **Log Group Name**: `/aws/ec2/data_processing_logs`

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Install Dependencies

Create a `requirements.txt` file with the required Python packages:

```txt
pandas==1.3.5
snowflake-connector-python==2.7.8
boto3==1.18.5
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### 3. Environment Variables

Set the necessary environment variables for AWS credentials:

```bash
export AWS_ACCESS_KEY_ID=your-access-key-id
export AWS_SECRET_ACCESS_KEY=your-secret-access-key
```

## Dockerization

The application is containerized using Docker for consistent deployment.

- **Dockerfile**: Contains the instructions to build the Docker image.

## Jenkins CI/CD Pipeline

Jenkins is used for continuous integration and continuous deployment (CI/CD).

- **Jenkinsfile**: Defines the pipeline stages:
  - Checkout
  - Build Docker Image
  - Run Tests
  - Deploy to AWS using Terraform

## Terraform Automation

Terraform is used for infrastructure as code (IaC) to provision and manage AWS resources.

- **Terraform Files**:
  - `providers.tf`: AWS provider configuration
  - `ec2_instance.tf`: EC2 instance resource
  - `s3_bucket.tf`: S3 bucket resource
  - `cloudwatch_logs.tf`: CloudWatch Logs resource

## Usage

1. Run the Jenkins pipeline to automate the infrastructure setup and deployment.
2. Monitor the infrastructure and logs on AWS Console and CloudWatch.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

