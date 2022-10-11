import sys

T = int(sys.stdin.readline())
Yonsei, Korea = [], []
for i in range(T):
    for i in range(9):
        Y, K = map(int, sys.stdin.readline().split())
        Yonsei.append(Y)
        Korea.append(K)
    if sum(Yonsei) < sum(Korea):
        print("Korea")
    elif sum(Yonsei) > sum(Korea):
        print("Yonsei")
    elif sum(Yonsei) == sum(Korea):
        print("Draw")