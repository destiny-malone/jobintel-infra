provider "aws" {
  region = "us-west-2"
}

resource "random_id" "bucket_id" {
  byte_length = 4
}

resource "aws_s3_bucket" "resume_bucket" {
  bucket        = "${var.bucket_prefix}-${random_id.bucket_id.hex}"
  force_destroy = true # helpful during development
  # acl = "public-read"
}

# modern ownership controls where acl is no longer needed so we use bucket policy instead

resource "aws_s3_bucket_ownership_controls" "resume_ownership" {
  bucket = aws_s3_bucket.resume_bucket.id

  rule {
    object_ownership = "BucketOwnerEnforced"
  }
}

resource "aws_s3_bucket_public_access_block" "resume_public_block" {
  bucket = aws_s3_bucket.resume_bucket.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

resource "aws_s3_bucket_versioning" "resume_versioning" {
  bucket = aws_s3_bucket.resume_bucket.id

  versioning_configuration {
    status = "Enabled"
  }
}

# This sets up a secure, modern AWS S3 bucket for Terraform env in WSL using AWS IAM user/secure credentials
# Terraform script w/ ownership controls and public access blocks now deployed due to replacing deprecated ACLs
# Deployed infrastructure as code while being able to solve multi-real-world errors regarding initiation and applying
# of the S3 bucket with ownership controls and public access blocks