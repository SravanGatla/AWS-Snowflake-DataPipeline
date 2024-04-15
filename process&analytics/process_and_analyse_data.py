from your_module import JSONDataExtractor, CSVDataExtractor

class DataProcessor:
  def __init__(self, data):
    self.data = data

  def process_and_analyse_data(self):
    self.data['age'] = self.data['age'].astype(int)
    self.data['date'] = pd.to_datetime(self.data['date'])
    # Map 'gender' values to numeric values
    gender_mapping = {
            'male': 1,
            'female': 0,
            'Not Specified': 2
        }
    self.data['gender'] = self.data['gender'].map(gender_mapping).fillna(self.data['gender'])
    return self.data
