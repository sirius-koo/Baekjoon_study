T = int(input())
A_lst = []
B_lst = []
sum_lst = []
for i in range(0, T):
    A, B = map(int, input().split())
    A_lst.append(A)
    B_lst.append(B)
    sum_lst.append(A+B)
for i in range(0, T):
    print("Case #{}:".format(i + 1), A_lst[i], "+", B_lst[i], "=", sum_lst[i])