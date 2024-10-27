import os
import boto3
import logging
from pathlib import Path

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client('s3')

def lambda_handler(_event, _context):
    bucket_name = os.environ.get('S3_BUCKET_NAME')

    photos_dir = Path(__file__).parent / 'photos'

    for photo_path in photos_dir.glob('*'):
        if photo_path.is_file():
            try:
                s3_client.upload_file(
                    str(photo_path),
                    bucket_name,
                    f"uploads/{photo_path.name}"
                )
                logger.info(f"Uploaded {photo_path.name} to {bucket_name}")
            except Exception as e:
                logger.error(f"Error uploading {photo_path.name}: {str(e)}")

    return {
        'statusCode': 200,
        'body': 'Photo upload complete'
    }
