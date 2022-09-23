import sys

N = int(sys.stdin.readline())
M, sum_score = 0, 0
set_score = []
score_list = list(map(int, sys.stdin.readline().split()))
M = max(score_list)
for i in range(len(score_list)):
    set_score.append(float(score_list[i]) / float(M) * 100)
for i in set_score:
    sum_score += i
result = sum_score / N
print(result)