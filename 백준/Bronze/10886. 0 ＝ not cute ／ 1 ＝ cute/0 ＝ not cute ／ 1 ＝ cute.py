import sys

N = int(sys.stdin.readline())
vote = []
o, z = 0, 0
for i in range(N):
    vote.append(int(sys.stdin.readline()))
for i in vote:
    if i == 1:
        o += 1
    else:
        z += 1
if o < z:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")