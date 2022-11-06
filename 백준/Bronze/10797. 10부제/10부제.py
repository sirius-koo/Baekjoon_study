import sys

day = int(sys.stdin.readline())
cnt = 0
car_number_list = list(map(int, sys.stdin.readline().split()))
for i in range(5):
    if (day == car_number_list[i]):
        cnt += 1
print(cnt)