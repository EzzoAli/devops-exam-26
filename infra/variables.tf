variable "bucket_name" {
  description = "S3 bucket name for storing images"
  type        = string
  default     = "pgr301-couch-explorers"
}

variable "candidate_number" {
  description = "Candidate number"
  type        = string
  default     = "26"
}

variable "alarm_email" {
  description = "Email address to receive CloudWatch alarm notifications"
  type        = string
}
