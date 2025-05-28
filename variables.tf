variable "access_key" {
  type        = string
  description = "AWS access key"
  sensitive = true # sensitive variable to avoid exposing credentials
  default     = "" # default can be empty, but should be set in a secure way
  validation {
    condition     = length(var.access_key) > 0
    error_message = "AWS access key must not be empty."
  }
}

variable "secret_key" {
  type        = string
  description = "AWS secret key"
  sensitive   = true # sensitive variable to avoid exposing credentials
  default     = "" # default can be empty, but should be set in a secure way
  validation {
    condition     = length(var.secret_key) > 0
    error_message = "AWS secret key must not be empty."
  }
}
variable "region" {
  description = "The AWS region to deploy the resources"
  type        = string
}

variable "bucket_prefix" {
  description = "The prefix for the S3 bucket"
  type        = string
  default     = "jobintel-resume-bucket"
}