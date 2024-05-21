import unittest
from unittest.mock import patch, MagicMock
import asyncio
import os
from io import StringIO
import shutil
from mining_repositories.clone import clone_repository_async, clone_repositories_async, \
    get_repository_name


class TestCloneFunctions(unittest.TestCase):
    def setUp(self):
        self.repository1 = "https://github.com/ryojiagatsuma1004/CSVPrinter.git"
        self.repository2 = "https://github.com/ryojiagatsuma1004/CSVPrinterFail.git"
        self.cwd = os.path.dirname(__file__)
        self.directory1 = os.path.join(self.cwd, get_repository_name(self.repository1))
        self.directory2 = os.path.join(self.cwd, "abc")
        self.test_dirs = []

    def tearDown(self):
        # テスト後に生成されたディレクトリを削除
        for test_dir in self.test_dirs:
            if os.path.exists(test_dir):
                shutil.rmtree(test_dir)

    def test_get_repository_name_is_exist(self):
        name = get_repository_name(self.repository1)
        self.assertEqual(name, 'CSVPrinter')

    def test_get_repository_name_is_not_exist(self):
        with self.assertRaises(Exception) as e:
            get_repository_name('https://www.google.com')

        self.assertIn("Invalid repository URL:", str(e.exception))

    def test_clone_repository_async_exist_repo(self):
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(clone_repository_async(self.repository1))
        self.test_dirs.append(os.path.join(self.cwd, get_repository_name(self.repository1)))
        self.assertTrue(os.path.exists(os.path.join(self.cwd, get_repository_name(self.repository1))))

    def test_clone_repository_async_exist_repo_and_dir(self):
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(clone_repository_async(self.repository1, self.directory1))
        self.test_dirs.append(self.directory1)
        self.assertTrue(os.path.exists(self.directory1))

    def test_clone_repositories_async_exist_repo(self):
        repos = [
            {'repository': self.repository1, 'directory': self.directory2},
            {'repository': self.repository1}
        ]

        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(clone_repositories_async(repos))

        self.test_dirs.append(self.directory1)
        self.test_dirs.append(self.directory2)
        self.assertTrue(os.path.exists(self.directory1))
        self.assertTrue(os.path.exists(self.directory2))

    def test_clone_repositories_async_not_exist_repo(self):
        repos = [
            {'repository': self.repository2, 'directory': self.directory2},
            {'repository': self.repository2}
        ]

        # 標準エラー出力をキャプチャして、エラーメッセージが出力されているか確認
        with patch('sys.stderr', new_callable=StringIO) as mock_stderr:
            loop = asyncio.get_event_loop()
            result = loop.run_until_complete(clone_repositories_async(repos))
            self.assertIn('Failed to clone', mock_stderr.getvalue())


if __name__ == '__main__':
    unittest.main()
