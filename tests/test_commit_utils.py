import unittest
from unittest.mock import patch, Mock
import mining_repositories.commit_utils as cu

class TestCommitUtils(unittest.TestCase):
    
    @patch('commit_utils.subprocess.run')
    def test_get_commit_ids_success(self, mock_run):
        # Arrange
        mock_run.return_value = Mock(returncode=0, stdout=b'commit1\ncommit2\ncommit3\n', stderr=b'')
        expected_commit_ids = ['commit1', 'commit2', 'commit3']

        # Act
        actual_commit_ids = cu.get_commit_ids('dummy_path')

        # Assert
        self.assertEqual(expected_commit_ids, actual_commit_ids)

    @patch('commit_utils.subprocess.run')
    def test_get_commit_ids_failure(self, mock_run):
        # Arrange
        mock_run.return_value = Mock(returncode=1, stdout=b'', stderr=b'error message')

        # Act & Assert
        with self.assertRaises(Exception) as context:
            cu.get_commit_ids('dummy_path')

        self.assertTrue('error message' in str(context.exception))


    def test_compare_commit_sets(self):
        set_a = {"a", "b", "c"}
        set_b = {"b", "c", "d"}
        expected_result = {"d"}
        actual_result = cu.compare_commit_sets(set_a, set_b)
        self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main()