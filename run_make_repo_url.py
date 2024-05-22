import json
import sys


def main():
    forks_list = json.load(sys.stdin)
    rl = []
    for i in forks_list:
        print(i["html_url"])


if __name__ == '__main__':
    main()
