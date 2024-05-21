# usage: cat fork.json | python run_count_forks.py > count.txt

import sys
import json
import mining_repositories.fork as mrf
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, help='fork list of the repository (JSON file)')
    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r') as f:
            forks_list = json.load(f)
    else:
        forks_list = json.load(sys.stdin)

    try:
        count = mrf.count_forks(forks_list)
        print(count)
    except json.JSONDecodeError:
        print("input data is not a json format", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
