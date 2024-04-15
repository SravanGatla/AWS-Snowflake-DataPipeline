from your_module import DataProcessor

class DataMasker:
  def __init__(self, processed_data):
    self.processed_data = processed_data

 # There are various other columns which are masked depending on the columns and nature of data. But, in this method I took some basic columns 
  def mask_sensitive_data(self):
    def mask_ssn_or_account(x, column_name):
      if isinstance(x,str) and column_name in ['SSN', 'account_number']:
        return 'X' * len(x)
      else:
        return x


    masked_data = [chunk.applymap(lambda x: mask_ssn_or_account(x, column_name)) for column_name, chunk in self.processed_data.items()]
    return masked_data
