resource "aws_cloudwatch_metric_alarm" "sqs_oldest_message_alarm" {
  alarm_name          = "SQS_OldestMessage_Alarm_26"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 1
  metric_name         = "ApproximateAgeOfOldestMessage"
  namespace           = "AWS/SQS"
  period              = 60
  statistic           = "Maximum"
  threshold           = 30

  alarm_description = "Triggered when the oldest message in the SQS queue exceeds 5 minutes"
  dimensions = {
    QueueName = aws_sqs_queue.image_gen_queue.name
  }

  actions_enabled     = true
  alarm_actions       = [aws_sns_topic.sqs_delay_alarm_topic.arn]
  ok_actions          = [aws_sns_topic.sqs_delay_alarm_topic.arn]
}
