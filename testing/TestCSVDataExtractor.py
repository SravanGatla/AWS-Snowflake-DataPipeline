import pytest
from your_module import CSVDataExtractor
from S3Fetcher import S3Fetcher

class TestCSVDataExtractor:
    @pytest.fixture
    def example_csv_data(self):
        return S3Fetcher.fetch_csv_data('your-test-bucket-name', 'test-file.csv')

    def test_extract_data(self, example_csv_data):
        extractor = CSVDataExtractor('test-bucket', 'test-file.csv')
        result = extractor.extract_data()

        assert len(result) == 1
        assert result[0].equals(example_csv_data)

if __name__ == "__main__":
    pytest.main()
