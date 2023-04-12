#!/usr/bin/env python3
import re
import sys

if __name__ == "__main__":
    regex = r'^(feat|fix|docs|style|refactor|perf|test|chore)(\s(feat|fix|docs|style|refactor|perf|test|chore))*\([^\)]+\):\s.+$'
    commit_message_file = sys.argv[1]
    message = open(commit_message_file).read().strip()

    if not re.match(regex, message):
        print("Error: Not a valid commit message! Please follow git commit guidelines")
        sys.exit(1)
