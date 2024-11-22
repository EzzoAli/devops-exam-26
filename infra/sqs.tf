resource "aws_sqs_queue" "image_gen_queue" {
  name                      = "image-gen-queue-26"
  visibility_timeout_seconds = 120
}
