from your_module import DataMasker
from snowflake.connector import connect, ProgrammingError
from snowflake.connector.pandas_tools import write_pandas

class SnowflakeLoader:
  def __init__(self, processed_data, snowflake_connection_params, table_name):
    self.processed_data = processed_data
    self.snowflake_connection_params = snowflake_connection_params
    self.table_name = table_name

  def load_data_to_snowflake(self):
    try:
      conn = connect(**self.snowflake_connection_params)
      create_stage_query = f"CREATE OR REPLACE STAGE XXXXXX_external_stage"
      conn.cursor().execute(create_stage_query)

      for i, chunk in enumerate(self.processed_data):
        stage_file_path = f"/data_chunk_{i}.csv"
        write_pandas(conn, chunk, stage_name = 'XXXXXX_external_stage', table_name = stage_file_path)

      copy_into_table_query = f"COPY INTO {self.table_name} FROM '@XXXXXX_external_stage' FILE_FORMAT = (TYPE = CSV)"
      conn.cursor().execute(copy_into_table_query)
      conn.commit()
      print("Data Loaded into Snowflake successfully.")
    except ProgrammingError as e:
     print("Error:", e)

