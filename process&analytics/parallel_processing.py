from your_module import process_and_analyse_data, mask_sensitive_data, load_data_to_snowflake

def process_data_in_parallel(process, data):
  return process.process_and_analyse_data(data)

def mask_data_in_parallel(process, data):
  return process.mask_sensitive_data(data)

def load_data_in_parallel(process, data):
  return process.load_data_in_parallel(data)
