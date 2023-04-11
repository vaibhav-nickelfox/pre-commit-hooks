import re
import sys

def feat(message):
    regex = r'^(feat|fix|docs|style|refactor|perf|test|chore)(\s(feat|fix|docs|style|refactor|perf|test|chore))*\([^\)]+\):\s.+$'
    match = re.match(regex, message)
    if match:
        return True
    else:
        return False

if __name__ == "__main__":
    message = sys.argv[1]
    if feat(message):
        print("Message follows regex pattern!")
    else:
        print("Message does not follow regex pattern.")
