from your_module import DataExtractor

class CSVDataExtractor(DataExtractor):
  def extract_data(self):
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket = self.bucket_name, key = self.file_key)
    chunks = pd.read_csv(obj['Body'], lines = True, chunksize = self.chunk_size)
    data_chunks = []
    for i, chunk in enumerate(chunks):
      data_chunks.append(chunk)
    return data_chunks
