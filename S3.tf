# S3 Bucket
resource "aws_s3_bucket" "data_bucket" {
  bucket = "your-s3-bucket-name" # Update with your bucket name
  acl    = "private"

  tags = {
    Name        = "DataBucket"
    Environment = "Production"
  }
}
