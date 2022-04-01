T = int(input())
sum_lst = []
for i in range(0, T):
    A, B = map(int, input().split())
    sum_lst.append(A+B)
for i in range(0, T):
    print("Case #{}:".format(i + 1), sum_lst[i])