# README

このコード群はGitHub上のフォークリポジトリを分析する目的で作成．

## 使用例

```bash
# インストール及びテスト実行は省略可
# スクリプトをインストール
# pip install -e .
# テスト実行
# python setup.py test

# REPO_FULL_NAME をフォークしているリポジトリのリストを取得
python run_list_forks.py -e ENV_GITHUBH_TOKEN -r REPO_FULL_NAME > forks.json
# フォークリポジトリ数をカウント
cat forks.json | python run_count_forks.py > autoware_forks_count.txt
# フォークリポジトリをクローン
cat forks.json | python run_clone_repositories.py
```

## json ファイルのフォーマット

フォークリポジトリのリストを以下のjsonファイルのフォーマットで表現．

キーに"full_name"，"html_url"があれば分析可能．

```json
[
  {
    "full_name": "tokoroten32/tmp2024",
    "html_url": "https://github.com/tokoroten32/tmp2024",
    "owner": {
      "login": "tokoroten32",
      "id": 84116002,
      "avatar_url": "https://avatars.githubusercontent.com/u/84116002?v=4",
      "url": "https://api.github.com/users/tokoroten32"
    },
    "description": null,
    "forks_count": 0,
    "stargazers_count": 0,
    "watchers_count": 0,
    "open_issues_count": 0,
    "created_at": "2024-04-22T07:42:56+00:00",
    "updated_at": "2024-04-22T07:42:57+00:00"
  },
  {
    "full_name": "ryojiagatsuma1004/tmp2024",
    "html_url": "https://github.com/ryojiagatsuma1004/tmp2024",
    "owner": {
      "login": "ryojiagatsuma1004",
      "id": 167161796,
      "avatar_url": "https://avatars.githubusercontent.com/u/167161796?v=4",
      "url": "https://api.github.com/users/ryojiagatsuma1004"
    },
    "description": null,
    "forks_count": 0,
    "stargazers_count": 0,
    "watchers_count": 0,
    "open_issues_count": 0,
    "created_at": "2024-04-22T07:42:54+00:00",
    "updated_at": "2024-05-20T12:40:13+00:00"
  }
]

```

## ファイル構成

```bash
├── README.md
├── mining_repositories: ライブラリ
│  ├── __init__.py
│  ├── clone.py
│  ├── fork.py
│  └── utils.py
├── run_clone_repositories.py: リポジトリのリストから全リポジトリをクローンするスクリプト
├── run_count_forks.py: フォークリポジトリ数をカウントするスクリプト
├── run_list_forks.py: リポジトリのフォークを取得するスクリプト
├── setup.py
├── tests: ライブラリのテスト
│  ├── __init__.py
│  ├── mock_forks.json
│  ├── test_clone.py
│  ├── test_forks.py
│  └── test_utils.py
```

## TODO

- ドキュメントの整備
- 変更されたコミットのファイル名を取得するスクリプトの作成
    - コミットIDを取得するコードを作成
    - コミットIDの差を見るコードを作成
    - 変更があったリポジトリとコミットIDのリストを取得するコードを作成
