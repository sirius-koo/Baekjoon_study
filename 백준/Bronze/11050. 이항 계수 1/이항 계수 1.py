import sys


def factorial(n):
    output = 1

    for i in range(1, n + 1):
        output *= i

    return output


def bino_coefficient(x, y):
    return factorial(x) // (factorial(x - y) * factorial(y))


N, K = map(int, sys.stdin.readline().split())
print(bino_coefficient(N, K))