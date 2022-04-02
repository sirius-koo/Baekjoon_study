N, M = input().split()
first_cut = int(N) - 1
Second_cut = int(N) * (int(M) - 1)
print(first_cut + Second_cut)
'''
N X M 크기의 조각을 최소 횟수로 자를 때
처음으로 N-1번을 자르면 1xM 크기의 조각 N개가 생긴다.
그 다음으로 자를 땐 M-1번이 아니라, N개 조각 하나 씩 잘라야 한다.
따라서 N * (M - 1)
'''
