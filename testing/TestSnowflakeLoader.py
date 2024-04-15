import pytest
from your_module import SnowflakeLoader
from S3Fetcher import S3Fetcher
from unittest.mock import patch, MagicMock

class TestSnowflakeLoader:
    @pytest.fixture
    def example_data(self):
        return S3Fetcher.fetch_csv_data('your-test-bucket-name', 'test-file.csv')

    @patch('snowflake.connector.connect')
    def test_load_data_to_snowflake(self, mock_connect, example_data):
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor

        loader = SnowflakeLoader([example_data], {}, 'test_table')
        loader.load_data_to_snowflake()

        assert mock_cursor.execute.called
        assert mock_cursor.commit.called

if __name__ == "__main__":
    pytest.main()
