import sys

T = int(sys.stdin.readline())
roomnumber = 0

for _ in range(T):
    front, back = 0, 0
    H, W, N = map(int, sys.stdin.readline().split())

    if N % H != 0:
        front = N % H
        back = int(N / H) + 1
    else:
        front = H
        back = int(N / H)

    if back < 10:
        print(int(str(front) + "0" + str(back)))
    else:
        print(int(str(front) + "" + str(back)))