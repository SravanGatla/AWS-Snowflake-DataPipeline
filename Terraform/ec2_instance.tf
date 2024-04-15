resource "aws_instance" "data_processing_instance" {
  ami           = "your-ami-id"
  instance_type = "t2.micro"

  tags = {
    Name = "DataProcessingInstance"
  }
}
