a = [0]*5
for i in range(5):
    a[i] = int(input())
    if a[i] < 40:
        a[i] = 40
avg = sum(a) / 5
print(int(avg))