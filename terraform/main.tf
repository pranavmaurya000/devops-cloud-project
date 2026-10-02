terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }

  required_version = ">= 1.6.0"
}

provider "aws" {
  region = "ap-south-1"
}

resource "aws_s3_bucket" "devops_project" {
  bucket = "devops-cloud-project-172575864548"

  tags = {
    Name        = "DevOps Cloud Project"
    Environment = "Dev"
    ManagedBy   = "Terraform"
  }
}