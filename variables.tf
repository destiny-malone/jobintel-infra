variable "region" {
  description = "The AWS region to deploy the resources"
  type        = string
  default     = "us-west-2"
}

variable "bucket_prefix" {
  description = "The prefix for the S3 bucket"
  type        = string
  default     = "jobintel-resume-bucket"
}