import unittest
from unittest.mock import patch, MagicMock
import asyncio
import os
from io import StringIO
import shutil
from mining_repositories.clone import clone_repository_async, clone_repositories_async, \
    get_repository_name
import tempfile


class TestCloneFunctions(unittest.TestCase):
    def setUp(self):
        self.exist_repo = "https://github.com/ryojiagatsuma1004/CSVPrinter.git"
        self.not_exist_repo = "https://github.com/ryojiagatsuma1004/CSVPrinterFail.git"
        self.cwd = os.getcwd()

    def tearDown(self):
        os.chdir(self.cwd)

    def test_get_repository_name_exist_repo_name(self):
        name = get_repository_name(self.exist_repo)
        self.assertEqual(name, 'CSVPrinter')

    def test_get_repository_name_not_exist_repo_name(self):
        with self.assertRaises(Exception) as e:
            get_repository_name('https://www.google.com')
        self.assertIn("Invalid repository URL:", str(e.exception))

    def test_clone_repository_async_exist_repo(self):
        semaphore = asyncio.Semaphore(4)
        loop = asyncio.get_event_loop()
        temp_dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, temp_dir)
        os.chdir(temp_dir)
        result = loop.run_until_complete(clone_repository_async(semaphore, self.exist_repo))
        self.assertTrue(os.path.exists(os.path.join(temp_dir, get_repository_name(self.exist_repo))))

    def test_clone_repository_async_exist_repo_and_dir(self):
        semaphore = asyncio.Semaphore(4)
        temp_dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, temp_dir)
        os.chdir(temp_dir)
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(
            clone_repository_async(semaphore, self.exist_repo, os.path.join(temp_dir, "tcraerad")))
        self.assertTrue(os.path.exists(os.path.join(temp_dir, "tcraerad")))

    def test_clone_repositories_async_exist_repo(self):
        temp_dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, temp_dir)
        os.chdir(temp_dir)

        repos = [
            {'repository': self.exist_repo, 'directory': os.path.join(temp_dir, "tcraer")},
            {'repository': self.exist_repo}
        ]

        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(clone_repositories_async(repos))

        self.assertTrue(os.path.exists(os.path.join(temp_dir, "tcraer")))
        self.assertTrue(os.path.exists(os.path.join(temp_dir, "CSVPrinter")))

    def test_clone_repositories_async_not_exist_repo(self):
        temp_dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, temp_dir)
        os.chdir(temp_dir)

        repos = [
            {'repository': self.not_exist_repo, 'directory': os.path.join(temp_dir, "tcraer")},
            {'repository': self.not_exist_repo}
        ]

        # 標準エラー出力をキャプチャして、エラーメッセージが出力されているか確認
        with patch('sys.stderr', new_callable=StringIO) as mock_stderr:
            loop = asyncio.get_event_loop()
            result = loop.run_until_complete(clone_repositories_async(repos))
            self.assertIn('Failed to clone', mock_stderr.getvalue())

    def test_clone_repositories_async_can_clone_40_repo(self):
        temp_dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, temp_dir)
        os.chdir(temp_dir)

        repos = []
        for i in range(40):
            repos.append({'repository': self.exist_repo, 'directory': os.path.join(temp_dir, str(i))})

        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(clone_repositories_async(repos))

        for i in repos:
            self.assertTrue(os.path.exists(i['directory']))

    def test_clone_repositories_async_can_clone_100_repo_10_parallel(self):
        temp_dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, temp_dir)
        os.chdir(temp_dir)

        repos = []
        for i in range(100):
            repos.append({'repository': self.exist_repo, 'directory': os.path.join(temp_dir, str(i))})

        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(clone_repositories_async(repos, max_parallel=10))

        for i in repos:
            self.assertTrue(os.path.exists(i['directory']))


if __name__ == '__main__':
    unittest.main()
