import sys

cnt = 0
N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())
for i in data:
    if i == v:
        cnt += 1
    else:
        cnt = cnt

print(cnt)