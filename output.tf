output "bucket_name" {
  description = "Name of the S3 bucket"
  value       = aws_s3_bucket.resume_bucket.bucket
}
output "bucket_arn" {
  description = "ARN of the resume bucket"
  value       = aws_s3_bucket.resume_bucket.arn
}
output "region" {
  description = "The AWS region where the bucket is deployed"
  value       = var.region
}

output "access_key" {
  description = "AWS access key"
  value       = var.access_key
  sensitive   = true # sensitive output to avoid exposing credentials
}

output "secret_key" {
  description = "AWS secret key"
  value       = var.secret_key
  sensitive   = true # sensitive output to avoid exposing credentials
}

# ARN is the Amazon Resource Name, a unique (exact/full) identifier (ID) for AWS resources (buckets) to attach policies/permissions
# The bucket name is the unique name of the S3 bucket