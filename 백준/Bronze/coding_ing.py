#BOJ_11022
#A + B 구현을 어떻게 해야할지 고민중!
T = int(input())
sum_lst = []
for i in range(0, T):
    A, B = map(int, input().split())
    A_lst = A.split()
    B_lst = B.split()
    sum_lst.append(A+B)
for i in range(0, T):
    print("Case #{}:".format(i + 1), A_lst[i], "+", B_lst[i], ":", sum_lst[i])
...
