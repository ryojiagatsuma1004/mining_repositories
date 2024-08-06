import unittest
from datetime import datetime
from unittest.mock import patch
import mining_repositories.utils as mru


class TestGenerateTimestamp(unittest.TestCase):

    @patch('mining_repositories.utils.datetime')
    def test_generate_timestamp(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2023, 5, 17, 15, 45, 30)
        mock_datetime.strftime = datetime.strftime

        expected_timestamp = "2023-05-17-15-45-30"
        actual_timestamp = mru.generate_timestamp()

        self.assertEqual(expected_timestamp, actual_timestamp)


if __name__ == '__main__':
    unittest.main()
