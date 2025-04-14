#!/bin/bash

BASE_DIR="./services"
OUTPUT_FILE="./compiled_output.md"

> "$OUTPUT_FILE"

find "$BASE_DIR" -type f -name "*.md" | while read -r FILE; do
    REL_DIR=$(dirname "${FILE#$BASE_DIR}")
    DIR_NAME=$(basename "$REL_DIR")
    FILE_NAME=$(basename "$FILE")

    # Add directory header (skip if top-level)
    if [ "$REL_DIR" != "." ]; then
        echo -e "\n# $DIR_NAME" >> "$OUTPUT_FILE"
    fi

    # Add file header
    echo -e "\n## $FILE_NAME" >> "$OUTPUT_FILE"

    # Append file content
    cat "$FILE" >> "$OUTPUT_FILE"
done
