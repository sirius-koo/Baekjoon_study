import sys

T = int(sys.stdin.readline())
for i in range(T): #
    sp = list(sys.stdin.readline().rstrip().split())
    num = float(sp[0])
    for i in range(len(sp)):
        if sp[i] == '@':
            num *= 3
        elif sp[i] == '%':
            num += 5
        elif sp[i] == '#':
            num -= 7
    print('{:.2f}'.format(num))