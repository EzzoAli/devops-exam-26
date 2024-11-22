resource "aws_lambda_function" "image_gen_lambda" {
  filename         = "lambda.zip" # Replace with the actual zip file
  function_name    = "image-gen-lambda-26"
  role             = aws_iam_role.lambda_execution_role.arn
  handler          = "lambda_sqs.lambda_handler"
  runtime          = "python3.8"
  timeout          = 60  # Increase timeout to 30 seconds
  memory_size      = 512

  environment {
    variables = {
      BUCKET_NAME      = var.bucket_name
      CANDIDATE_NUMBER = var.candidate_number
    }
  }

  source_code_hash = filebase64sha256("lambda.zip")
}

resource "aws_lambda_event_source_mapping" "lambda_sqs" {
  event_source_arn  = aws_sqs_queue.image_gen_queue.arn
  function_name     = aws_lambda_function.image_gen_lambda.arn
  batch_size        = 10
  enabled           = true
}
