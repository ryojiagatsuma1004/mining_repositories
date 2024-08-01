from github import Github
from github import GithubException


def list_forks(github_instance, repo_full_name):
    try:
        # リポジトリの情報取得
        repo = github_instance.get_repo(repo_full_name)
    except GithubException as e:
        raise Exception(f"リポジトリ '{repo_full_name}' の情報取得に失敗しました。詳細: {e}")

    forks = repo.get_forks()

    # フォーク一覧をリストに変換
    forks_list = []
    for fork in forks:
        fork_info = {
            'full_name': fork.full_name,
            'html_url': fork.html_url,
            'owner': {
                'login': fork.owner.login,
                'id': fork.owner.id,
                'avatar_url': fork.owner.avatar_url,
                'url': fork.owner.url
            },
            'description': fork.description,
            'forks_count': fork.forks_count,
            'stargazers_count': fork.stargazers_count,
            'watchers_count': fork.watchers_count,
            'open_issues_count': fork.open_issues_count,
            'created_at': fork.created_at.isoformat(),
            'updated_at': fork.updated_at.isoformat()
        }
        forks_list.append(fork_info)

    return forks_list


def count_forks(forks_list):
    if isinstance(forks_list, list):
        # フォークの長さを返す
        return len(forks_list)
    else:
        raise ValueError("引数 forks_list はリスト型である必要があります。")


def count_forks_branchs(forks_list):
    if isinstance(forks_list, list):
        count = 0
        # フォークの長さを返す
        for fork in forks_list:
            if len(fork["branches"]) > 1:
                count += 1
        return count
    else:
        raise ValueError("引数 forks_list はリスト型である必要があります。")
