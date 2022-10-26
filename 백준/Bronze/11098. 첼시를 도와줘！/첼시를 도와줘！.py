import sys

C_li, name_li = [], []
n = int(sys.stdin.readline())
for i in range(n):
    p = int(sys.stdin.readline())
    for i in range(p):
        C, name = map(str, sys.stdin.readline().split())
        C_li.append(C)
        name_li.append(name)
    C_li = list(map(int, C_li))
    print(name_li[C_li.index(max(C_li))])
    C_li.clear()
    name_li.clear()