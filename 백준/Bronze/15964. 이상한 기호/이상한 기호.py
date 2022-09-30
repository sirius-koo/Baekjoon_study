import sys

def sign(a, b):
    x, y = 0, 0
    x = a + b
    y = a - b
    return (x * y)

A, B = map(int, sys.stdin.readline().split())
print(sign(A, B))