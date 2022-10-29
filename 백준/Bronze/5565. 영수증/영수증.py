import sys

total = int(sys.stdin.readline())
sum_ = 0
for i in range(9):
    price = int(sys.stdin.readline())
    sum_ += price
print(total - sum_)