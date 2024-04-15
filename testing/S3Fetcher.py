import boto3
import pandas as pd

class S3Fetcher:
    @staticmethod
    def fetch_csv_data(bucket_name, file_key):
        s3 = boto3.client('s3')
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        content = response['Body'].read().decode('utf-8')
        return pd.read_csv(pd.compat.StringIO(content))

    @staticmethod
    def fetch_json_data(bucket_name, file_key):
        s3 = boto3.client('s3')
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        content = response['Body'].read().decode('utf-8')
        return pd.read_json(pd.compat.StringIO(content))
