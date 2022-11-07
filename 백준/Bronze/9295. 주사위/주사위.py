import sys

T = int(sys.stdin.readline())
for i in range(1, T + 1):
    dice = list(map(int, sys.stdin.readline().split()))
    print("Case {}:".format(i), sum(dice))
