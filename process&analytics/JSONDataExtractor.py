from your_module import DataExtractor

class JSONDataExtractor(DataExtractor):
  def extract_data(self):
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket = self.bucket_name, file_key = self.file_key)
    chunks = pd.read_json(obj['Body'], lines = True, chunks = self.chunk_size)
    data_chunks = []
    for i, chunk in enumerate(chunks):
      data_chunks.append(chunk)
    return data_chunks
