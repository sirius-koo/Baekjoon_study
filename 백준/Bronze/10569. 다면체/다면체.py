import sys

T = int(sys.stdin.readline())
for i in range(T):
    V, E = map(int, sys.stdin.readline().split())
    result = 2 - (V - E)
    if result > 0:
        print(result)
    else:
        print(result * (-1))