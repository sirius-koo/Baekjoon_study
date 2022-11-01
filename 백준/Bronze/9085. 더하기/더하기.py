import sys

T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    print(sum(a))