resource "aws_s3_bucket" "data_bucket" {
  bucket = "your-s3-bucket-name"
  acl    = "private"

  tags = {
    Name        = "DataBucket"
    Environment = "Production"
  }
}
