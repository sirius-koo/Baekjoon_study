import sys

opt = []
T = int(sys.stdin.readline())
for i in range(T):
    s = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    for i in range(n):
        q, p = map(int, sys.stdin.readline().split())
        opt.append(q * p)
    print(s + sum(opt))
    opt.clear()