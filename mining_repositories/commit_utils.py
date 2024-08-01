import subprocess
import os


def get_commit_ids(repo_path):
    # リポジトリの全コミットIDを取得
    commit_ids = subprocess.run(["git", "log", "--pretty=format:%H"], cwd=repo_path, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
    if commit_ids.returncode != 0:
        raise Exception(commit_ids.stderr.decode('utf-8'))
    return list(commit_ids.stdout.decode('utf-8').splitlines())


def compare_commit_sets(set_a, set_b):
    return set_b - (set_a & set_b)


def and_commit_sets(set_a, set_b):
    return set_a & set_b


if __name__ == "__main__":
    # use get_commit_ids function to test
    repo_path = os.getcwd()
    print(get_commit_ids(repo_path))
    # use compare_commit_sets function to test
    set_a = {"a", "b", "c"}
    set_b = {"b", "c", "d"}
    print(compare_commit_sets(set_a, set_b))
