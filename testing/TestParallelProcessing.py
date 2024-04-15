import pytest
from your_module import DataProcessor, DataMasker, SnowflakeLoader
from S3Fetcher import S3Fetcher
from unittest.mock import patch

class TestParallelProcessing:
    @pytest.fixture
    def example_data(self):
        return S3Fetcher.fetch_csv_data('your-test-bucket-name', 'test-file.csv')

    def test_process_data_in_parallel(self, example_data):
        processor = DataProcessor(example_data)
        result = processor.process_data_in_parallel()
        assert result['age'].dtype == int
        assert result['date'].dtype == 'datetime64[ns]'

    def test_mask_data_in_parallel(self, example_data):
        masker = DataMasker([example_data])
        result = masker.mask_data_in_parallel()
        assert len(result) == 1
        assert result[0].equals(example_data)

    @patch('snowflake.connector.connect')
    def test_load_data_in_parallel(self, mock_connect, example_data):
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor

        loader = SnowflakeLoader([example_data], {}, 'test_table')
        loader.load_data_in_parallel()

        assert mock_cursor.execute.called
        assert mock_cursor.commit.called

if __name__ == "__main__":
    pytest.main()
