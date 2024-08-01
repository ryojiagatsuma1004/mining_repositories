# usage: python run_list_forks.py -e <GH_TOKEN> -r <owner>/<repo_name> > forks.json

import os
import argparse
from github import Github
import json
import mining_repositories.fork as mrb


def main():
    # 引数を解析
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--env', type=str, required=True, help='Access token for GitHub API')
    parser.add_argument('-r', '--repo', type=str, required=True, help='repository name (owner/repo_name)')
    args = parser.parse_args()

    # 環境変数からGitHubのアクセストークンを取得
    gh_token = os.environ.get(args.env)
    repo_name = args.repo

    # GitHubのアクセストークンを指定してGitHubインスタンスを作成
    github_instance = Github(gh_token)

    # リポジトリのフォーク一覧を取得
    forks_list = mrb.list_forks(github_instance, repo_name)
    # フォーク一覧をJSON形式で出力
    print(json.dumps(forks_list, indent=4))

    github_instance.close()


if __name__ == "__main__":
    main()
