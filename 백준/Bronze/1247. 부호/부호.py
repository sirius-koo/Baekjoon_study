import sys

num_li_sum, num_sum = [], 0
for i in range(3):
    N = int(sys.stdin.readline())
    for i in range(N):
        num = int(sys.stdin.readline())
        num_sum += num
    num_li_sum.append(num_sum)
    num_sum = 0
for i in range(3):
    if num_li_sum[i] == 0:
        print(0)
    elif num_li_sum[i] > 0:
        print("+")
    elif num_li_sum[i] < 0:
        print("-")