T = int(input())
numbers = list(map(int, input()))
sum_num = 0

for i in range(0, T):
    sum_num += int(numbers[i])

print(sum_num)