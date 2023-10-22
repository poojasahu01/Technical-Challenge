terraform {
  backend "s3" {
    bucket         = "object-to-store-tfstate-file"
    encrypt        = true
    key            = "terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "dynamoDB-terraform-backend"
  }
}
