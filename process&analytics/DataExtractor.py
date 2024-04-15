import boto3
import pandas as pd
from snowflake.connector import connect, PermissionError
from snowflake.connector.pandas_tools import write_pandas


class DataExtractor:
  def __init__(self, bucket_name, file_key, chunk_size = 10000):
    self.bucket_name = bucket_name
    self.file_key = file_key
    self.chunk_size = chunk_size

  def extract_data(self):
    raise NotImplementedError("Subclasses must implement extract_data method")

  def create_external_stage(self, conn, stage_name):
    cursor = conn.cursor()
    create_stage_query = f"create or replace stage data_XXXXXX_stage" 
    cursor.execute(create_stage_query)
