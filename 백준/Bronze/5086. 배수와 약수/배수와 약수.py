import sys

a, b = 1, 2
while (a != b):
    a, b = map(int, sys.stdin.readline().split())
    if (a == 0 and b == 0):
        break
    elif (b % a == 0):
        print("factor")
    elif (a % b == 0):
        print("multiple")
    else:
        print("neither")