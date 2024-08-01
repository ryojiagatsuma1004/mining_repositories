import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from github.GithubException import GithubException
import mining_repositories.fork as mrb
import os
import json


class TesFork(unittest.TestCase):
    def setUp(self):
        self.access_token = 'your_access_token'
        self.repo_full_name = 'owner/repo_name'

        # パッチャーを作成し、開始する
        self.github_patcher = patch('mining_repositories.fork.Github')
        self.mock_github_class = self.github_patcher.start()
        self.mock_github_instance = self.mock_github_class.return_value

    def tearDown(self):
        # パッチャーを停止する
        self.github_patcher.stop()

    def test_list_forks_is_exist(self):
        # リポジトリオブジェクトのモックを作成
        mock_repo = MagicMock()
        self.mock_github_instance.get_repo.return_value = mock_repo

        # get_forksメソッドのモックを作成
        mock_repo.get_forks.return_value = [
            MagicMock(
                full_name='user1/repo1',
                html_url='https://github.com/user1/repo1',
                owner=MagicMock(
                    login='user1',
                    id=123,
                    avatar_url='https://github.com/avatars/user1',
                    url='https://github.com/user1'
                ),
                description='A test repo',
                forks_count=5,
                stargazers_count=10,
                watchers_count=8,
                open_issues_count=1,
                created_at=datetime(2021, 1, 1, 0, 0, 0),
                updated_at=datetime(2021, 1, 2, 0, 0, 0)
            )
        ]
        # フォークリストを取得
        forks_list = mrb.list_forks(self.mock_github_instance, self.repo_full_name)

        # 期待される結果を読み込み
        expected_file_path = os.path.join(os.path.dirname(__file__), 'mock_forks.json')
        with open(expected_file_path, 'r') as f:
            expected_forks_list = json.load(f)

        # フォークリストが期待される結果と等しいか確認
        self.assertEqual(forks_list, expected_forks_list)

    def test_list_forks_original_repo_is_not_exist(self):
        self.mock_github_instance.get_repo.side_effect = GithubException(404, 'Not Found', None)

        with self.assertRaises(Exception) as context:
            mrb.list_forks(self.mock_github_instance, self.repo_full_name)

        self.assertIn("情報取得に失敗しました", str(context.exception))

    def test_count_forks_success(self):
        # 期待される結果を読み込み
        expected_file_path = os.path.join(os.path.dirname(__file__), 'mock_forks.json')
        with open(expected_file_path, 'r') as f:
            expected_forks_list = json.load(f)

        self.assertEqual(mrb.count_forks(expected_forks_list), len(expected_forks_list))

    def test_count_forks_is_not_list(self):
        obj = {'key': 'value'}
        with self.assertRaises(Exception) as e:
            mrb.count_forks(obj)
