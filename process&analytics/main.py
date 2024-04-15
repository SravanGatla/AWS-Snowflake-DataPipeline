import boto3
import pandas as pd
import multiprocessing
from snowflake.connector import connect,ProgrammingError
from your_module import CSVDataExtractor, JSONDataExtractor
from your_module import process_and_analyse_data, mask_sensitive_data, load_data_to_snowflake
from your_module import process_data_in_parallel, mask_data_in_parallel, load_data_in_parallel

def main():
  s3_bucket_name = 'XXXXXXX-data-bucket'
  S3_file_key = 'data/2024/customer_data.csv'
  snowflake_connection_params = {
      'user': 'SravankumarGatla_XXXXX',
      'password': 'XXXXXX',
      'account': 'xy12345.us-east-1',
      'warehouse': 'warehouseXXXX',
      'database': 'databaseXXXX',
      'schema': 'private'
  }
  table_name = 'table-name-XXXX'

  extractor = CSVDataExtractor(s3_bucket_name, S3_file_key)
  data_chunks = extractor.extract_data()

  processors = [DataProcessor(chunk) for chunk in data_chunks]
  with multiprocessing.Pool() as pool:
    processed_chunks = pool.starmap(process_data_in_parallel, zip(processors, data_chunks))

  maskers = [DataMasker(chunk) for chunk in processed_chunks]
  with multiprocessing.Pool() as pool:
    masked_chunks = pool.starmap(mask_data_in_parallel, zip(maskers, processed_chunks))

  snowflake_loaders = [SnowflakeLoader(chunk, snowflake_connection_params, table_name) for chunk in masked_chunks]
  with multiprocessing.Pool() as pool:
    pool.map(load_data_in_parallel, snowflake_loaders)

if __name__ == "__main__":
  main()
