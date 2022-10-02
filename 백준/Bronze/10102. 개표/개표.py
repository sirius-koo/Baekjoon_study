import sys

V = int(sys.stdin.readline())
vote = list(sys.stdin.readline().rstrip())

A, B = 0, 0
for v in vote:
    if v == 'A':
        A += 1
    else:
        B += 1
if A == B:
    print("Tie")
elif A > B:
    print("A")
elif A < B:
    print("B")