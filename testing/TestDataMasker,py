import pytest
from your_module import DataMasker
from S3Fetcher import S3Fetcher

class TestDataMasker:
    @pytest.fixture
    def example_data(self):
        return S3Fetcher.fetch_csv_data('your-test-bucket-name', 'test-file.csv')

    def test_mask_sensitive_data(self, example_data):
        masker = DataMasker([example_data])
        result = masker.mask_sensitive_data()

        assert len(result) == 1
        assert result[0].equals(example_data)

if __name__ == "__main__":
    pytest.main()
