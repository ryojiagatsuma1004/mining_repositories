# Usage: cat ./data/tmp.json | python3 ./run_compare_forks.py -b /workspace/data/

import json
import sys
import os

def main():
    repos = json.load(sys.stdin)
    
    # 出力用の箱を準備
    repos_with_changes = []
    autoware_ai = ["a90f6ae4713a3e49b13b8a788497e6f92926cdb6", "0ac26da20134ae8b6ccb60d3cf562a0f731d3abb"]
    count_aw = 0
    count_awai = 0
    for repo in repos:
        diff = set(autoware_ai) & set(repo["commit_diff"])
        if bool(diff):
            count_awai += 1
        else:
            count_aw += 1
            repos_with_changes.append(repo)
    
    # 結果を標準出力に表示
    print("autoware.ai fork repo is : ", count_awai)
    print("autoware fork repo have diff is: ", count_aw)
    print(json.dumps(repos_with_changes, indent=4))
        
if __name__ == "__main__":
    main()
    