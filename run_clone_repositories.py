# usage: cat fork.json | python run_clone_repositories.py

import mining_repositories.clone as clone
import mining_repositories.utils as utils
import json
import argparse
import os
import sys
import asyncio


def main():
    # 引数の解析
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, help='fork list of the repository (JSON file)')
    args = parser.parse_args()
    cwd = os.path.dirname(__file__)
    ctime = utils.generate_timestamp()
    base_dir = os.path.join(cwd, ctime, 'fork_repositories')

    # リポジトリリストの読み込み
    if args.file:
        with open(args.file, 'r') as f:
            forks_list = json.load(f)
    else:
        forks_list = json.load(sys.stdin)

    # リポジトリとクローン先のディレクトリのリストを作成
    repositories = []
    for fork in forks_list:
        repositories.append({
            'repository': fork['html_url'],
            'directory': os.path.join(base_dir, fork['full_name'])
        })

    # 非同期でクローン
    asyncio.run(clone.clone_repositories_async(repositories))


if __name__ == '__main__':
    main()
