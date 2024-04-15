import pytest
from your_module import JSONDataExtractor
from S3Fetcher import S3Fetcher

class TestJSONDataExtractor:
    @pytest.fixture
    def example_json_data(self):
        return S3Fetcher.fetch_json_data('your-test-bucket-name', 'test-file.json')

    def test_extract_data(self, example_json_data):
        extractor = JSONDataExtractor('test-bucket', 'test-file.json')
        result = extractor.extract_data()

        assert len(result) == 1
        assert result[0].equals(example_json_data)

if __name__ == "__main__":
    pytest.main()
