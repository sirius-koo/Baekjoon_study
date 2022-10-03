import sys

K, N, M = map(int, sys.stdin.readline().rstrip().split())
money = 0
money = M - (K * N)
if money < 0:
    money *= -1
    print(money)
elif money >= 0:
    print(0)