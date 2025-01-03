import base64
import boto3
import json
import random
import os

# Initialize AWS clients
bedrock_client = boto3.client("bedrock-runtime", region_name="us-east-1")
s3_client = boto3.client("s3")

# Model ID, bucket name, and candidate number
model_id = "amazon.titan-image-generator-v1"
bucket_name = os.environ.get("BUCKET_NAME")
candidate_number = os.environ.get("CANDIDATE_NUMBER")

def lambda_handler(event, context):
    try:
        # Parse the input prompt
        body = json.loads(event['body'])
        prompt = body.get("prompt")
        if not prompt:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Prompt is required"})
            }

        # Generate random seed and S3 path
        seed = random.randint(0, 2147483647)
        s3_image_path = f"{candidate_number}/generated_images/titan_{seed}.png"

        # Bedrock model payload
        native_request = {
            "taskType": "TEXT_IMAGE",
            "textToImageParams": {"text": prompt},
            "imageGenerationConfig": {
                "numberOfImages": 1,
                "quality": "standard",
                "cfgScale": 8.0,
                "height": 1024,
                "width": 1024,
                "seed": seed,
            }
        }

        # Call Bedrock model
        response = bedrock_client.invoke_model(
            modelId=model_id,
            body=json.dumps(native_request)
        )
        model_response = json.loads(response["body"].read())

        # Decode image data
        base64_image_data = model_response["images"][0]
        image_data = base64.b64decode(base64_image_data)

        # Upload image to S3
        s3_client.put_object(Bucket=bucket_name, Key=s3_image_path, Body=image_data)

        # Return S3 URI
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Image created successfully",
                "uri": f"s3://{bucket_name}/{s3_image_path}"
            })
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
