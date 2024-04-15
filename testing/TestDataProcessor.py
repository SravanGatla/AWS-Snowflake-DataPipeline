import pytest
from your_module import DataProcessor
from S3Fetcher import S3Fetcher

class TestDataProcessor:
    @pytest.fixture
    def example_data(self):
        return S3Fetcher.fetch_csv_data('your-test-bucket-name', 'test-file.csv')

    def test_process_and_analyze_data(self, example_data):
        processor = DataProcessor(example_data)
        result = processor.process_and_analyze_data()

        assert result['age'].dtype == int
        assert result['date'].dtype == 'datetime64[ns]'

if __name__ == "__main__":
    pytest.main()
