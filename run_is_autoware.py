# Usage: cat ./data/tmp.json | python3 ./run_compare_forks.py -b /workspace/data/

import mining_repositories.commit_utils as cu
import argparse
import json
import sys
import os


def main():
    # 引数の解析
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str)
    parser.add_argument('-b', '--basedir', type=str, help='fork dir of the repository')

    args = parser.parse_args()
    # 標準入力の処理
    if args.file:
        with open(args.file, 'r') as f:
            forks = json.load(f)
    else:
        forks = json.load(sys.stdin)

    if args.basedir:
        base_dir = args.basedir
    else:
        base_dir = os.path.dirname(__file__)

    # 出力用の箱を準備
    repos_with_changes = []
    # オリジナルリポジトリのコミットIDを取得
    original_cid = ["5b83044efd92ac913215a3cc5dd69aeb2e5f2705",
                    "ff87896549f0a916f15cf4705c1e313e0a6b240b",
                    "a90f6ae4713a3e49b13b8a788497e6f92926cdb6",
                    "0ac26da20134ae8b6ccb60d3cf562a0f731d3abb"]
    # フォークリポジトリの中で、親リポジトリと差分があるリポジトリを取得
    for fork in forks:
        try:
            fork_cid = cu.get_commit_ids(os.path.join(base_dir, fork["relative_path"]))
            commit_diff_set = cu.and_commit_sets(set(original_cid), set(fork_cid))
            if not bool(commit_diff_set):
                repos_with_changes.append(fork)
        except Exception as e:
            print(f"エラー: {e}", file=sys.stderr)
            continue

    # 結果を標準出力に表示
    print(json.dumps(repos_with_changes, indent=4))


if __name__ == "__main__":
    main()
