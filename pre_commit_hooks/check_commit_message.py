import re
import sys

def check(message):
    regex = r'^(feat|fix|docs|style|refactor|perf|test|chore)(\s(feat|fix|docs|style|refactor|perf|test|chore))*\([^\)]+\):\s.+$'
    match = re.match(regex, message)
    if match:
        return True
    else:
        return False

if __name__ == "__main__":
    commit_message_file = sys.argv[1]
    message = open(commit_message_file).read().strip()
    if check(message):
        print("Valid Commit message!")
    else:
        print("Not a valid commit message")
        print("Please follow git commit guidelines")
