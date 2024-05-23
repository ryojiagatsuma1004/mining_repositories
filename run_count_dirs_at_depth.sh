#!/bin/bash

# 引数の確認
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <parent_directory> <depth>"
    exit 1
fi

PARENT_DIR="$1"
DEPTH="$2"

# ディレクトリの存在確認
if [ ! -d "$PARENT_DIR" ]; then
    echo "Error: Directory $PARENT_DIR does not exist."
    exit 1
fi

# 負の数を入れていないか確認
if ! [[ "$DEPTH" =~ ^[0-9]+$ ]]; then
    echo "Depth must be a non-negative integer."
    exit 1
fi

# 指定された深さにあるディレクトリの数を数える
DIR_COUNT=$(find "$PARENT_DIR" -mindepth "$DEPTH" -maxdepth "$DEPTH" -type d | wc -l)

# 結果を表示
echo "Number of directories at depth $DEPTH: $DIR_COUNT"
