import sys
import json
import csv


def main():
    # JSONデータをパース
    data = json.load(sys.stdin)

    # commit_diffの個数でソート
    sorted_data = sorted(data, key=lambda x: len(x['commit_diff']), reverse=True)

    # CSV出力のためのヘッダー
    csv_header = ["html_url", "commit_diff"]

    # CSV出力
    csv_output = csv.writer(sys.stdout)
    csv_output.writerow(csv_header)

    for entry in sorted_data:
        html_url = entry["html_url"]
        commit_diff = ",".join(entry["commit_diff"])
        csv_output.writerow([html_url, commit_diff])


if __name__ == '__main__':
    main()
