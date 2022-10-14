import sys

A, B = 100, 100
n = int(sys.stdin.readline())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if a < b:
        A -= b
    elif a > b:
        B -= a
    else:
        pass
print(A)
print(B)