import sys
listA, listC = [], []
cnt = {}
B = 42
for i in range(10):
    listA.append(int(sys.stdin.readline()))
for i in range(10):
    listC.append(listA[i] % B)
for i in listC:
    try:
        cnt[i] += 1
    except:
        cnt[i] = 1
print(len(cnt))