import sys

list_n, list_30, list_set = [], [], []

for i in range(1, 30 + 1):
    list_30.append(i)
for i in range(28):
    list_n.append(int(sys.stdin.readline()))

list_set = list(set(list_30) - set(list_n))
print(min(list_set))
print(max(list_set))