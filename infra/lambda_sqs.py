import os
import random
import boto3
import base64
import json

# AWS Clients
bedrock_client = boto3.client("bedrock-runtime", region_name="us-east-1")
s3_client = boto3.client("s3")

# Constants
MODEL_ID = "amazon.titan-image-generator-v1"
BUCKET_NAME = os.environ["BUCKET_NAME"]
CANDIDATE_NUMBER = os.environ["CANDIDATE_NUMBER"]

def lambda_handler(event, context):
    for record in event["Records"]:
        try:
            # Extract the SQS message body
            prompt = record["body"]
            seed = random.randint(0, 2147483647)

            # S3 path using CANDIDATE_NUMBER
            s3_image_path = f"{CANDIDATE_NUMBER}/images/titan_{seed}.png"

            # Prepare the request for image generation
            native_request = {
                "taskType": "TEXT_IMAGE",
                "textToImageParams": {"text": prompt},
                "imageGenerationConfig": {
                    "numberOfImages": 1,
                    "quality": "standard",
                    "cfgScale": 8.0,
                    "height": 512,
                    "width": 512,
                    "seed": seed,
                },
            }

            # Invoke the model
            response = bedrock_client.invoke_model(
                modelId=MODEL_ID,
                body=json.dumps(native_request)
            )

            # Parse the response and decode the image
            model_response = json.loads(response["body"].read())
            base64_image_data = model_response["images"][0]
            image_data = base64.b64decode(base64_image_data)

            # Upload the image to S3
            s3_client.put_object(Bucket=BUCKET_NAME, Key=s3_image_path, Body=image_data)

        except Exception as e:
            print(f"Error processing record: {record}. Error: {e}")

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Processing completed"})
    }
