import boto3
from dotenv import load_dotenv
import os
load_dotenv()

s3=boto3.client('s3')
file_path1=os.getenv('file_path1')
file_path2=os.getenv('file_path2')
bucket_name=os.getenv('bucket_name')
s3_key=os.getenv('s3_key')

s3.upload_file(
    file_path2,
    bucket_name,
    s3_key
)
print("file uploaded successfully")
