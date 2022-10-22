import sys

N_rev = []
while True:
    N = list(map(int, sys.stdin.readline().rstrip()))
    if N == [0]:
        break
    N_rev = N[::-1]
    if N == N_rev:
        print("yes")
    else:
        print("no")