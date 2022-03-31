#아직 끝내지 못한 코드
#BOJ_11021
T = int(input())
for i in range(0, T):
    sum_list = []
    A, B = input().split()
    sum_list.append(int(A)+int(B))
for i in range(1, T + 1):
    print("Case #{}: ".format(i), sum_list[i - 1])
