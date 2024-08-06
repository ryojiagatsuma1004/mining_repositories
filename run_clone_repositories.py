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
    parser.add_argument('-p', '--parallel', type=str, help='Number of parallel clone (default is 4)')
    args = parser.parse_args()
    cwd = os.path.dirname(__file__)
    ctime = utils.generate_timestamp()
    base_dir = os.path.join(cwd, ctime)

    # リポジトリリストの読み込み
    if args.file:
        with open(args.file, 'r') as f:
            forks_list = json.load(f)
    else:
        forks_list = json.load(sys.stdin)

    # 並列クローン数の指定があれば読み取る
    if args.parallel:
        max_parallel = args.parallel
    else:
        max_parallel = 4

    # リポジトリとクローン先のディレクトリのリストを作成
    repositories = []
    for fork in forks_list:
        repositories.append({
            'repository': fork['html_url'],
            'directory': os.path.join(base_dir, fork['full_name'])
        })

    # 非同期でクローン
    asyncio.run(clone.clone_repositories_async(repositories, max_parallel=max_parallel))


if __name__ == '__main__':
    main()
