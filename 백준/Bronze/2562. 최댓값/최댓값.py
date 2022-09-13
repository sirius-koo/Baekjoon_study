data = []
for i in range(1, 10):
    data.append(int(input()))
max_num = max(data)
max_num_index = data.index(max_num) + 1
print(max(data))
print(max_num_index)