import sys

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    A, B = sys.stdin.readline().split()
    print(int(A) + int(B))