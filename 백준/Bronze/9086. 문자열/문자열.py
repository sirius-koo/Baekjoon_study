import sys

T = int(sys.stdin.readline())
for i in range(T):
    w = list(sys.stdin.readline().rstrip())
    print(w[0]+w[len(w)-1])