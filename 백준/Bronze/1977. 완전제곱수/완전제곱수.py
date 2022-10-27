import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
perfect_li = []
for i in range(M, N + 1, 1):
    if (i == int(i ** 0.5) ** 2):
        perfect_li.append(i)
if (perfect_li == []):
    print(-1)
else:
    print(sum(perfect_li))
    print(min(perfect_li))