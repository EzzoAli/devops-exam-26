output "sqs_queue_url" {
  value = aws_sqs_queue.image_gen_queue.id
}

output "lambda_function_arn" {
  value = aws_lambda_function.image_gen_lambda.arn
}

output "sns_topic_arn" {
  value = aws_sns_topic.sqs_delay_alarm_topic.arn
}

output "cloudwatch_alarm_name" {
  value = aws_cloudwatch_metric_alarm.sqs_oldest_message_alarm.alarm_name
}
