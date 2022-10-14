import sys

word = list(sys.stdin.readline().rstrip())
word_re = word[::-1]

if word == word_re:
    print(1)
else:
    print(0)