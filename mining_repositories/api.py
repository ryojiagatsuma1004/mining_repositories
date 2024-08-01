from github import Github
from github import GithubException
import os
import argparse
import sys

def list_branches(github_instance, repo_full_name):
    try:
        # リポジトリの情報取得
        repo = github_instance.get_repo(repo_full_name)
    except GithubException as e:
        print(f"リポジトリ '{repo_full_name}' の情報取得に失敗しました。詳細: {e}", file=sys.stderr)
        return []

    try:
        branches = repo.get_branches()
    except GithubException as e:
        print(f"リポジトリ '{repo_full_name}' のブランチ情報取得に失敗しました。詳細: {e}", file=sys.stderr)
        return []

    # ブランチ一覧をリストに変換
    branches_list = []
    for branch in branches:
        branch_info = {
            'name': branch.name,
            'commit': {
                'sha': branch.commit.sha,
                'url': branch.commit.url
            }
        }
        branches_list.append(branch_info)

    return branches_list