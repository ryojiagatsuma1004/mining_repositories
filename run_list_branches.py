# usage: cat ai2023.json |  python3 run_list_branches.py -e ENV_GITHUBH_TOKEN > forks.json

import os
import argparse
from github import Github
import json
import mining_repositories.api as mrb
import sys


def main():
    # 引数を解析
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--env', type=str, required=True, help='Access token for GitHub API')
    parser.add_argument('-f', '--file', type=str, help='fork list of the repository (JSON file)')
    args = parser.parse_args()

    # リポジトリリストの読み込み
    if args.file:
        with open(args.file, 'r') as f:
            forks_list = json.load(f)
    else:
        forks_list = json.load(sys.stdin)

    # 環境変数からGitHubのアクセストークンを取得
    gh_token = os.environ.get(args.env)

    # GitHubのアクセストークンを指定してGitHubインスタンスを作成
    github_instance = Github(gh_token)

    repositories = []

    for fork in forks_list:
        # リポジトリのフォーク一覧を取得
        branches = mrb.list_branches(github_instance, fork['full_name'])
        fork['branches'] = branches
        repositories.append(fork)
    
    print(json.dumps(repositories, indent=4))
    github_instance.close()


if __name__ == "__main__":
    main()
