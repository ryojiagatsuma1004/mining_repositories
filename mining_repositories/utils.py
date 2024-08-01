from datetime import datetime


def generate_timestamp():
    # 現在時刻を取得
    now = datetime.now()
    # 各部分をフォーマットしてハイフンで接続
    timestamp = now.strftime('%Y-%m-%d-%H-%M-%S')
    return timestamp
