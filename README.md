# README

このコード群はGitHub上のフォークリポジトリを分析する目的で作成．

## 使用例

```bash
# インストール及びテスト実行は省略可
##スクリプトをインストール
python3 -m venv venv
source ./venv/bin/activate
python3 -m pip install --upgrade pip
pip install -e .
## テスト実行
python3 setup.py test

# 変数の定義
REPO_FULL_NAME=NAME
FORKS=FILENAME.json
BASEDIR=DIR
HAVE_DIFF=DIFF.json
ORIGINAL_REPO=DIR
AW=DIR
AWAI=DIR

# 実行
## REPO_FULL_NAME をフォークしているリポジトリのリストを取得
python3 run_list_forks.py -e ENV_GITHUBH_TOKEN -r $REPO_FULL_NAME > $FORKS
## フォークリポジトリをクローン
cat $FORKS | python3 run_clone_repositories.py
## クローン出来たリポジトリの情報で json を更新
cat $FORKS | python3 run_sync_clone_repos.py -b $BASEDIR > $BASEDIR/$FORKS
## オリジナルリポジトリとフォークリポジトリを比較，オリジナルリポジトリリポジトリよりコミットが進んでいるフォークリポジトリのみを抽出
cat $BASEDIR/$FORKS | python3 run_compare_forks.py --original $ORIGINAL_REPO -b $BASEDIR > $HAVE_DIFF
## csvに変換
cat $HAVE_DIFF | python3 run_json2csv.py > $FORKS.csv

# その他
## フォークリポジトリ数をカウント
cat $FORKS | python3 run_count_forks.py
## クローン出来たリポジトリの数を出力
./run_count_dirs_at_depth.sh ./fork_repositories 2
## Autoware のリポジトリを出力
cat $BASEDIR/$FORKS | python3 run_is_autoware.py -b $AW > $BASEDIR/autoware-$FORKS
## Autoware AI のリポジトリを出力
cat $BASEDIR/$FORKS | python3 run_is_autoware_ai.py -b $AWAI > $BASEDIR/autoware-ai-$FORKS
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
├── run_make_repo_url.py: json2csv
├── setup.py
├── tests: ライブラリのテスト
│  ├── __init__.py
│  ├── mock_forks.json
│  ├── test_clone.py
│  ├── test_forks.py
│  └── test_utils.py
```


