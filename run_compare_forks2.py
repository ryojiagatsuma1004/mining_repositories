# Usage: cat ./data/tmp.json | python3 ./run_compare_forks.py -b /workspace/data/

import mining_repositories.commit_utils as cu
import argparse
import json
import sys
import os

def main():
    # get the current working directory
    base_dir = os.getcwd()
    repos = json.load(sys.stdin)
    repos_with_changes = []
    autoware_ai = ["5b83044efd92ac913215a3cc5dd69aeb2e5f2705",
        "ff87896549f0a916f15cf4705c1e313e0a6b240b",
        "a90f6ae4713a3e49b13b8a788497e6f92926cdb6",
        "0ac26da20134ae8b6ccb60d3cf562a0f731d3abb"]
    diffc = 0
    # オリジナルリポジトリのコミットIDを取得
    orignal_cid = cu.get_commit_ids(os.path.join(base_dir,"2024-05-23-00-31-56/original_repository/autowarefoundation/autoware_ai"))
    # フォークリポジトリの中で、親リポジトリと差分があるリポジトリを取得
    for repo in repos:
        diff = set(autoware_ai) & set(repo["commit_diff"])
        if bool(diff):
            commit_diff_set = cu.compare_commit_sets(set(orignal_cid), set(repo["commit_diff"]))
            if bool(commit_diff_set):
                repo['commit_diff'] = list(commit_diff_set)
                repos_with_changes.append(repo)
                diffc += 1
    
    # 結果を標準出力に表示
    print("autoware.ai fork repo have diff is: ", diffc)
    print(json.dumps(repos_with_changes, indent=4))
        
if __name__ == "__main__":
    main()
    