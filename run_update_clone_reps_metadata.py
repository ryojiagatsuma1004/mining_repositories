import json
import os
import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, help='fork list of the repository (JSON file)')
    parser.add_argument('-b', '--basedir', type=str, help='fork dir of the repository')
    args = parser.parse_args()
    rp = ''

    if args.file:
        with open(args.file, 'r') as f:
            forks_list = json.load(f)
    else:
        forks_list = json.load(sys.stdin)

    if args.basedir:
        base_dir = os.path.join(os.path.dirname(__file__), args.basedir)
        rp = args.basedir
    else:
        base_dir = os.path.dirname(__file__)

    updated_fork_repos = []

    for repo in forks_list:
        if os.path.isdir(os.path.join(base_dir, repo['full_name'])):
            repo['relative_path'] = os.path.relpath(rp, repo['full_name'])
            updated_fork_repos.append(repo)

    print(json.dumps(updated_fork_repos, indent=4))


if __name__ == '__main__':
    main()
